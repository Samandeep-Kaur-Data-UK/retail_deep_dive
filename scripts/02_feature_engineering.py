from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEANED_PATH = PROJECT_ROOT / "data" / "cleaned" / "retail_cleaned.csv"
RFM_OUTPUT_PATH = PROJECT_ROOT / "data" / "cleaned" / "rfm_base.csv"
ENRICHED_OUTPUT_PATH = PROJECT_ROOT / "data" / "cleaned" / "retail_enriched.csv"


def main() -> None:
    print("Loading data...")
    df = pd.read_csv(CLEANED_PATH)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    print("Adding Revenue, Month, DayOfWeek, and Hour...")
    df["Revenue"] = df["Quantity"] * df["Price"]
    df["Month"] = df["InvoiceDate"].dt.month
    df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()
    df["Hour"] = df["InvoiceDate"].dt.hour

    print("Calculating RFM...")
    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    df["Days_Ago"] = (snapshot_date - df["InvoiceDate"]).dt.days

    rfm = df.groupby("Customer ID").agg(
        Recency=("Days_Ago", "min"),
        Frequency=("Invoice", "nunique"),
        Monetary=("Revenue", "sum"),
    ).reset_index()

    print(f"\nSnapshot date for Recency: {snapshot_date.date()}")
    print(f"RFM computed for {rfm.shape[0]:,} customers")
    print(rfm.head(10))
    print("\nRFM Summary Stats:")
    print(rfm[["Recency", "Frequency", "Monetary"]].describe().round(2))

    RFM_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rfm.to_csv(RFM_OUTPUT_PATH, index=False)
    print(f"\nSaved to: {RFM_OUTPUT_PATH}")

    df.to_csv(ENRICHED_OUTPUT_PATH, index=False)
    print(df.head(5).to_string())
    print(df.columns.tolist())


if __name__ == "__main__":
    main()
