from airflow.decorators import task

@task
def transform(file_path):

    df = pd.read_csv(file_path)

    logger.info("========== BEFORE ==========")
    logger.info(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove null values
    df = df.dropna()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Lowercase column names
    df.columns = df.columns.str.lower()

    logger.info("========== AFTER ==========")
    logger.info(df)

    output_path = f"{OUTPUT_PATH}/customers_clean.csv"

    df.to_csv(output_path, index=False)
    logger.info(f"Clean file saved to: {output_path}")

    return output_path
