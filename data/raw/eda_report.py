from pathlib import Path

import pandas as pd


RAW_PATH = Path(__file__).resolve().parent / "online_retail_II.xlsx"


def main() -> None:
    df = pd.read_excel(RAW_PATH)

    print("1. Null Counts Per Column:")
    print(df.isnull().sum())

    print("\n2. Unique Customer Count:")
    print(df["Customer ID"].nunique())

    print("\n3. Negative Quantities (Returns):")
    print(len(df[df["Quantity"] < 0]))

    print("\n4. Cancelled Orders (Invoices starting with 'C'):")
    print(len(df[df["Invoice"].astype(str).str.startswith("C", na=False)]))


if __name__ == "__main__":
    main()
