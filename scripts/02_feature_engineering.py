import pandas as pd

# 1. Simple Paths
input_file  = "/Users/saman/projects/retail_deep_dive/data/cleaned/retail_cleaned.csv"
output_file = "/Users/saman/projects/retail_deep_dive/data/cleaned/rfm_base.csv"

# 2. Load Data
print("Loading data...")
df = pd.read_csv(input_file)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 3. Feature Engineering - Add New Columns
print("Adding Revenue, Month, DayOfWeek, and Hour...")
df["Revenue"]   = df["Quantity"] * df["Price"]
df["Month"]     = df["InvoiceDate"].dt.month
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()
df["Hour"]      = df["InvoiceDate"].dt.hour

# 4. Calculate RFM
print("Calculating RFM...")
snapshot_date  = df["InvoiceDate"].max() + pd.Timedelta(days=1)
df["Days_Ago"] = (snapshot_date - df["InvoiceDate"]).dt.days

rfm = df.groupby("Customer ID").agg(
    Recency   = ("Days_Ago", "min"),
    Frequency = ("Invoice",  "nunique"),
    Monetary  = ("Revenue",  "sum")
).reset_index()

# 5. Preview & Export
print(f"\nSnapshot date for Recency: {snapshot_date.date()}")
print(f"RFM computed for {rfm.shape[0]:,} customers")
print(rfm.head(10))
print("\nRFM Summary Stats:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe().round(2))

rfm.to_csv(output_file, index=False)
print(f"\nSaved to: {output_file}")

# Save the full enriched dataframe before RFM collapse
df.to_csv("data/cleaned/retail_enriched.csv", index=False)
print(df.head(5).to_string())
print(df.columns.tolist())