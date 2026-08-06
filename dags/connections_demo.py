from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime


def show_connection():
    conn = BaseHook.get_connection("postgres_default")

    print("=" * 50)
    print(f"Host: {conn.host}")
    print(f"Database: {conn.schema}")
    print(f"User: {conn.login}")
    print(f"Port: {conn.port}")
    print("=" * 50)


with DAG(
    dag_id="connections_demo",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    PythonOperator(
        task_id="show_connection",
        python_callable=show_connection,
    )
