from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="extract_raw_to_gcs",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["zoomcamp", "thermal", "extract"],
) as dag:

    extract_and_upload = BashOperator(
        task_id="extract_and_upload",
        bash_command="python /opt/airflow/scripts/extract_and_upload.py",
    )
