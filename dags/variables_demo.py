from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


def read_variable():
    # قراءة أول Variable
    file_path = Variable.get("customer_file")

    # قراءة ثاني Variable
    company = Variable.get("company_name")

    print("=" * 50)
    print("Customer File Path:")
    print(file_path)

    print("=" * 50)
    print("Company Name:")
    print(company)

    print("=" * 50)


with DAG(
    dag_id="variables_demo",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    read_variable_task = PythonOperator(
        task_id="read_variable",
        python_callable=read_variable,
    )
