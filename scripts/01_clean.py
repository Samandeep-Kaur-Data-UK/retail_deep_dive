from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail_II.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "data" / "cleaned" / "retail_cleaned.csv"


def main() -> None:
    print("Loading data... this may take a minute.")
    df = pd.read_excel(RAW_PATH)
    print(f"Raw rows loaded: {len(df):,}")

    df = df.dropna(subset=["Customer ID"])
    print(f"After dropping null Customer ID: {len(df):,} rows")

    df = df.drop_duplicates()
    print(f"After removing duplicates: {len(df):,} rows")

    df = df[~df["Invoice"].astype(str).str.startswith("C", na=False)]
    print(f"After removing cancellations: {len(df):,} rows")

    df = df[df["Quantity"] > 0]
    print(f"After removing negative quantities: {len(df):,} rows")

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nCleaned data exported to: {OUTPUT_PATH}")
    print(f"Final row count: {len(df):,}")


if __name__ == "__main__":
    main()
