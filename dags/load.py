from airflow.decorators import task 
    
@task
def load(file_path):

    conn = None
    cursor = None

    try:

        hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)

        conn = hook.get_conn()

        cursor = conn.cursor()

        sql_path = f"{SQL_PATH}/create_tables.sql"

        with open(sql_path, "r") as file:
            create_table_sql = file.read()

        cursor.execute(create_table_sql)

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO customers
                (customer_id, first_name, last_name, email, country)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (customer_id)
                DO NOTHING
                """,
                (
                    int(row["customer_id"]),
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["country"],
                ),
            )

        conn.commit()

        logger.info("Customers Loaded Successfully")

    except Exception as e:

        logger.error(f"Load Task Failed: {e}")
        logger.error(traceback.format_exc())

        raise

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()
