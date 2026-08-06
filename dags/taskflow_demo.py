from airflow import DAG
from airflow.decorators import task
from datetime import datetime


with DAG(
    dag_id="taskflow_demo",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    @task
    def extract():
        print("Extracting Data...")
        return [1, 2, 3, 4, 5]

    @task
    def transform(data):
        print("Received Data:")
        print(data)

        transformed = [x * 10 for x in data]

        return transformed

    @task
    def load(data):
        print("Loading Data...")
        print(data)

    data = extract()

    transformed_data = transform(data)

    load(transformed_data)
