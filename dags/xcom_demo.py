from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract():
    print("Extracting data...")
    return ["Ali", "Omar", "Sara"]


def transform(ti):
    data = ti.xcom_pull(task_ids="extract")

    print("=" * 50)
    print("Data received from Extract:")
    print(data)
    print("=" * 50)


with DAG(
    dag_id="xcom_demo",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    extract_task >> transform_task
