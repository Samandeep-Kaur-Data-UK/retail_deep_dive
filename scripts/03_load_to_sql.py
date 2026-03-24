import pandas as pd
import sqlite3
from pathlib import Path

# --- Paths ---
cleaned_path = Path("data/cleaned/retail_cleaned.csv")
db_path = Path("data/retail.db")

# --- Load cleaned CSV ---
df = pd.read_csv(cleaned_path)

# --- Write to SQLite ---
conn = sqlite3.connect(db_path)
df.to_sql("transactions", conn, if_exists="replace", index=False)
conn.close()

print(f"Done. {len(df):,} rows loaded into 'transactions' table.")
print(f"DB saved to: {db_path.resolve()}")