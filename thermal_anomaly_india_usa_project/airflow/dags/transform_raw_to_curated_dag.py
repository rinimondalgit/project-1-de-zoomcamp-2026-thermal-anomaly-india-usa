from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="transform_raw_to_curated",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["zoomcamp", "thermal", "transform"],
) as dag:

    spark_transform = BashOperator(
        task_id="spark_transform",
        bash_command="python /opt/airflow/spark/transform_to_parquet.py",
    )
