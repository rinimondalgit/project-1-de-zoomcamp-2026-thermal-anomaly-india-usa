from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="load_curated_to_bigquery",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["zoomcamp", "thermal", "load"],
) as dag:

    load_to_bigquery = BashOperator(
        task_id="load_to_bigquery",
        bash_command="python /opt/airflow/scripts/load_to_bigquery.py",
    )
