FROM apache/airflow:2.8.1-python3.10

USER root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc g++ build-essential unixodbc-dev && \
    apt-get clean

USER airflow

# Install pinned versions (correct syntax for version constraints)
RUN pip install --no-cache-dir \
    apache-airflow==2.8.1 \
    apache-airflow-providers-microsoft-mssql \
    "apache-airflow-providers-openlineage>=1.4.0,<1.8.0"  # Wrap in quotes!
