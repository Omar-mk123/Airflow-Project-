from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data"
OUTPUT_PATH = BASE_DIR / "output"
SQL_PATH = BASE_DIR / "sql"

POSTGRES_CONN_ID = "postgres_default"
