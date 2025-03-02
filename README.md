# 📈 Stock Market Data Pipeline

This project demonstrates the construction of a data pipeline using **Apache Airflow** to process and analyze stock market data.

## 🚀 Overview

The pipeline performs the following tasks:

- **⚙️ Data Orchestration**: The Entire pipeline is orchestrated using Apache Airflow
- **📥 Data Extraction**: Retrieves stock market data from external stock data [Yahoo Finance API]
- **📦 Data Storage**: Storing the data in **Minio** (S3 like bucket)
- **🔄 Data Transformation**: Cleans and processes the extracted data using **Apache Spark**
- **🗄️ Data Loading**: Stores the transformed data into a **Postgres** database for analysis
- **📊 Data Analysis**: Analyzing the data using Metabase 

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&style=flat-square) 
![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apacheairflow&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&style=flat-square)
![Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?logo=apachespark&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white&style=flat-square)
![MinIO](https://img.shields.io/badge/MinIO-C12127?logo=minio&logoColor=white&style=flat-square)
![Metabase](https://img.shields.io/badge/Metabase-509EE3?logo=metabase&logoColor=white&style=flat-square)

## 📂 Project Structure

- **`dags/`**: Contains Airflow DAGs defining the ETL pipeline.
- **`include/`**: Stores the tasks file which contains python functions that are executed through airflow and used in the dags/ folder
- **`spark/`**: Includes Apache Spark scripts for large-scale data processing.
- **`tests/`**: Contains test cases to validate DAG execution.

## 🐳 Getting Started

To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/justinjsd/stock-market-data-pipeline.git
   cd stock-market-data-pipeline
