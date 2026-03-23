import pandas as pd

# ── 1. Load raw data ──────────────────────────────────────────────
file_path = '/Users/saman/projects/retail_deep_dive/data/raw/online_retail_II.xlsx'

print("Loading data... this may take a minute.")
df = pd.read_excel(file_path)
print(f"Raw rows loaded: {len(df):,}")

# ── 2. Drop rows with no Customer ID ─────────────────────────────
df = df.dropna(subset=['Customer ID'])
print(f"After dropping null Customer ID: {len(df):,} rows")

# ── 3. Remove duplicate rows ──────────────────────────────────────
df = df.drop_duplicates()
print(f"After removing duplicates: {len(df):,} rows")

# ── 4. Remove cancellations (Invoice starting with 'C') ───────────
df = df[~df['Invoice'].astype(str).str.startswith('C', na=False)]
print(f"After removing cancellations: {len(df):,} rows")

# ── 5. Remove negative quantities (returns) ───────────────────────
df = df[df['Quantity'] > 0]
print(f"After removing negative quantities: {len(df):,} rows")

# ── 6. Parse InvoiceDate to datetime ──────────────────────────────
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ── 7. Export cleaned data ────────────────────────────────────────
output_path = '/Users/saman/projects/retail_deep_dive/data/cleaned/retail_cleaned.csv'
df.to_csv(output_path, index=False)
print(f"\nCleaned data exported to: {output_path}")
print(f"Final row count: {len(df):,}")