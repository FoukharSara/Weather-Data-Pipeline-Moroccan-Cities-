from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from docker.types import Mount
from airflow.providers.docker.operators.docker import DockerOperator




default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    'description': "Weather Data Pipeline",
}

dag =  DAG(
    "orchestration_weather_api_dbt",
    default_args=default_args,
    catchup=False,
    schedule= timedelta(minutes=1),
)
def data_ingestion():
    from utils.insert_data import main
    return main()
 
with dag:   
    #task1
    task1 = PythonOperator(
        task_id="ingesting_data",
        python_callable=data_ingestion,
    )
    #task2
    
    task2 = DockerOperator(
        task_id="dbt_run",
        image="fishtownanalytics/dbt:1.0.0",
        command="run",
        docker_url="unix://var/run/docker.sock",
        network_mode="weatherdatapipeline_morccan_confluent",
        working_dir="/usr/app/dbt_project",
        mounts=[
            Mount(
                source="C:/Users/x1 carbon/Desktop/Weather Data Pipeline_Morccan/dbt_project",
                target="/usr/app/dbt_project",
                type="bind"
            ),
            Mount(
                source="C:/Users/x1 carbon/Desktop/Weather Data Pipeline_Morccan/profiles.yml",
                target="/root/.dbt/profiles.yml",
                type="bind"
            )
                
        ],
        auto_remove='success',
    )
    
    task1 >> task2
