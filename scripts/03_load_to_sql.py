import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEANED_PATH = PROJECT_ROOT / "data" / "cleaned" / "retail_cleaned.csv"
DB_PATH = PROJECT_ROOT / "data" / "retail.db"


def main() -> None:
    df = pd.read_csv(CLEANED_PATH)

    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql("transactions", conn, if_exists="replace", index=False)
    finally:
        conn.close()

    print(f"Done. {len(df):,} rows loaded into 'transactions' table.")
    print(f"DB saved to: {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()
