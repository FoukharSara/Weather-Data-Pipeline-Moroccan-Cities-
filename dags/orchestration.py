from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator



default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    'description': "Weather Data Pipeline",
}

dag =  DAG(
    "orchestration_weather",
    default_args=default_args,
    catchup=False,
    schedule_interval="@daily",
)
def data_ingestion():
    from utils.insert_data import main
    return main()
 
with dag:   
    #task1
    task1 = PythonOperator(
        task_id="streaming_data",
        python_callable=data_ingestion,
    )
    #task2
