from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import pandas as pd
import logging
import traceback

from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load
from tasks.validate import validate

from config import (
    DATA_PATH,
    OUTPUT_PATH,
    SQL_PATH,
    POSTGRES_CONN_ID,
)

logger = logging.getLogger(__name__)

default_args = {
    "owner": "Gony",
    "depends_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ETL", "PostgreSQL", "Pandas"],
) as dag:
    


   
    # ---------------- Pipeline ---------------- #

    raw_file = extract()

    clean_file = transform(raw_file)

    load_task = load(clean_file)

    validate_task = validate()

    load_task >> validate_task
