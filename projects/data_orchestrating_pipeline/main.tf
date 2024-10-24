provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "airflow" {
  metadata {
    name = "airflow"
  }
}

resource "kubernetes_persistent_volume_claim" "airflow_data_pvc" {
  metadata {
    name      = "airflow-data-pvc"
    namespace = kubernetes_namespace.airflow.metadata[0].name
  }
  spec {
    access_modes = ["ReadWriteOnce"]
    resources {
      requests = {
        storage = "1Gi"
      }
    }
  }
}

resource "kubernetes_deployment" "airflow" {
  metadata {
    name      = "airflow"
    namespace = kubernetes_namespace.airflow.metadata[0].name
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "airflow"
      }
    }
    template {
      metadata {
        labels = {
          app = "airflow"
        }
      }
      spec {
        container {
          name  = "airflow"
          image = "apache/airflow:2.3.0"
          ports {
            container_port = 8080
          }
          volume_mount {
            name       = "airflow-data"
            mount_path = "/usr/local/airflow/data"
          }
        }
        volume {
          name = "airflow-data"
          persistent_volume_claim {
            claim_name = kubernetes_persistent_volume_claim.airflow_data_pvc.metadata[0].name
          }
        }
      }
    }
  }
}

resource "kubernetes_deployment" "dbt" {
  metadata {
    name      = "dbt"
    namespace = kubernetes_namespace.airflow.metadata[0].name
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "dbt"
      }
    }
    template {
      metadata {
        labels = {
          app = "dbt"
        }
      }
      spec {
        container {
          name  = "dbt"
          image = "dbt-labs/dbt:latest"
          volume_mount {
            name       = "airflow-data"
            mount_path = "/usr/local/airflow/data"
          }
        }
        volume {
          name = "airflow-data"
          persistent_volume_claim {
            claim_name = kubernetes_persistent_volume_claim.airflow_data_pvc.metadata[0].name
          }
        }
      }
    }
  }
}
