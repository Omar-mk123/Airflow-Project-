from airflow.decorators import task


@task
def extract():

    file_path = f"{DATA_PATH}/customers.csv"

    logger.info(f"Reading file: {file_path}")

    return file_path
