### README

# Data Orchestration Pipeline

## Overview

This project demonstrates a comprehensive data pipeline using Docker, Apache Airflow, dBT, Kubernetes, and Terraform. The pipeline ingests data, transforms it using dBT, splits the data for training and testing, calculates the mean squared error, generates a plot, and saves the results in a specified directory. The directory is overwritten each time the task is run to ensure the latest data is always available.

## Prerequisites

- **Docker**: Ensure Docker is installed on your local machine.
- **Docker Compose**: Ensure Docker Compose is installed.
- **Kubernetes**: Set up a Kubernetes cluster (Minikube or any other Kubernetes setup).
- **kubectl**: Install the kubectl command-line tool.
- **Terraform**: Install Terraform for infrastructure as code.
- **Python**: Ensure Python is installed for running the Airflow DAG.

## Requirements

- **Docker**: Used to run Apache Airflow and dBT containers.
- **Apache Airflow**: Orchestrates the data pipeline.
- **dBT**: Handles data transformation.
- **Kubernetes**: Manages containerized applications.
- **Terraform**: Automates the setup and management of infrastructure.

## Summary

The data pipeline performs the following tasks:
1. **Data Ingestion**: Ingests data and saves it as `feature_data_raw.csv`.
2. **Data Transformation**: Uses dBT to clean and transform the data.
3. **Data Splitting and Model Training**: Splits the data into training and testing sets, trains a linear regression model, and evaluates it.
4. **Result Generation**: Calculates the mean squared error, generates a plot, and saves the results.
5. **Resource Management**: Ensures that all services are started and stopped as needed to prevent unnecessary resource usage.

## Setup

### Step 1: Docker Setup
1. Create a `docker-compose.yml` file to set up Airflow and dBT containers.
2. Start the Docker containers using `docker-compose up -d`.
3. Stop the Docker containers using `docker-compose down`.

### Step 2: Apache Airflow Setup
1. Create a DAG file `data_pipeline.py` in the `dags` folder.
2. Start Docker containers and access the Airflow web interface at `http://localhost:8080`.
3. Trigger the `data_pipeline` DAG to start the workflow.
4. Monitor the tasks in the Airflow web interface.

### Step 3: dBT Setup
1. Create a `dbt` project with the necessary structure.
2. Define the project configuration in `dbt_project.yml`.
3. Set up the profiles in `profiles.yml`.
4. Write the transformation logic in `models/transform.sql`.

### Step 4: Kubernetes Deployment
1. Create a Kubernetes deployment file `airflow-deployment.yml`.
2. Create a PersistentVolumeClaim `airflow-data-pvc.yml`.
3. Deploy the resources to Kubernetes using `kubectl apply`.

### Step 5: Terraform Setup
1. Create a Terraform configuration file `main.tf`.
2. Initialize Terraform using `terraform init`.
3. Apply the Terraform configuration using `terraform apply -auto-approve`.

## Running the Pipeline
1. Ensure Docker containers are running.
2. Access the Airflow web interface and trigger the `data_pipeline` DAG.
3. Monitor the workflow to ensure tasks complete successfully.

## Notes
- The setup ensures that all services are started and stopped as needed, preventing unnecessary resource usage.
- While the tools themselves are free to use, running these services, especially on cloud providers, may incur costs based on the resources consumed.