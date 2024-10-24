from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime
import os
import shutil
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import matplotlib.pyplot as plt

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 10, 23),
    "retries": 1,
}


def extract_data():
    np.random.seed(0)
    data = np.random.choice(
        [2, 3, 4, 5, 6, 7, 8, 9, 10],
        size=(1000, 10),
        p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2],
    )
    df = pd.DataFrame(data, columns=[f"feature_{i}" for i in range(1, 11)])
    df.to_csv("/usr/local/airflow/data/feature_data_raw.csv", index=False)


def calculate_data():
    output_dir = "/usr/local/airflow/data/data_orchestration_pipeline"

    # Ensure the output directory exists and is empty before saving new files
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    df = pd.read_csv("/usr/local/airflow/data/feature_data.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color="blue")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], "k--", lw=4)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted")
    plt.savefig(os.path.join(output_dir, "prediction_plot.png"))

    # Saving the root mean squared error and accuracy
    with open(os.path.join(output_dir, "rmse_output.txt"), "w") as f:
        f.write(f"Root Mean Squared Error: {rmse}\n")
        f.write(f"R^2 Score (Accuracy): {r2}\n")


with DAG("data_pipeline", default_args=default_args, schedule_interval="@daily") as dag:
    start_docker_container = BashOperator(
        task_id="start_docker_container", bash_command="docker-compose up -d"
    )

    extract_data_task = PythonOperator(
        task_id="extract_data", python_callable=extract_data
    )

    transform_data_task = BashOperator(
        task_id="transform_data", bash_command="dbt run --project-dir /usr/app/dbt"
    )

    calculate_data_task = PythonOperator(
        task_id="calculate_data", python_callable=calculate_data
    )

    save_data_task = BashOperator(
        task_id="save_data",
        bash_command='echo "Data saved to data_orchestration_pipeline directory"',
    )

    stop_docker_container = BashOperator(
        task_id="stop_docker_container", bash_command="docker-compose down"
    )

    start_kubernetes_pod = KubernetesPodOperator(
        task_id="start_kubernetes_pod",
        name="start_kubernetes_pod",
        namespace="default",
        image="apache/airflow:2.3.0",
        cmds=["bash", "-cx"],
        arguments=["echo", "Starting Kubernetes Pod"],
    )

    stop_kubernetes_pod = KubernetesPodOperator(
        task_id="stop_kubernetes_pod",
        name="stop_kubernetes_pod",
        namespace="default",
        image="apache/airflow:2.3.0",
        cmds=["bash", "-cx"],
        arguments=["echo", "Stopping Kubernetes Pod"],
    )

    (
        start_docker_container
        >> extract_data_task
        >> transform_data_task
        >> calculate_data_task
        >> save_data_task
        >> stop_docker_container
        >> start_kubernetes_pod
        >> stop_kubernetes_pod
    )
