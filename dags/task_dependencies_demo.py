from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def say_hello():
    print("Hello Airflow!")


with DAG(
    dag_id="task_dependencies_demo",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")

    hello = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )

    show_date = BashOperator(
        task_id="show_date",
        bash_command="date",
    )

    end = EmptyOperator(task_id="end")

    start >> hello >> show_date >> end
