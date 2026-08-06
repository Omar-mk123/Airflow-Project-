from airflow.decorators import task

@task
def validate():

    conn = None
    cursor = None

    try:

        hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)

        conn = hook.get_conn()

        cursor = conn.cursor()

        sql_path = f"{SQL_PATH}/validation.sql"

        with open(sql_path, "r") as file:
            validation_sql = file.read()

        cursor.execute(validation_sql)

        count = cursor.fetchone()[0]

        logger.info("=" * 50)
        logger.info(f"Total Rows = {count}")
        logger.info("=" * 50)

        if count == 0:
            raise ValueError(
                "Validation Failed: customers table is empty!"
            )

        logger.info("Validation Passed Successfully")

    except Exception as e:

        logger.error(f"Validation Task Failed: {e}")
        logger.error(traceback.format_exc())

        raise

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()
