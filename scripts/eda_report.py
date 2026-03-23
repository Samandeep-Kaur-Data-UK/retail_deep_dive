import pandas as pd

# Load the data from the correct project path
file_path = '/Users/saman/projects/retail_deep_dive/data/raw/online_retail_II.xlsx'

print("Loading data... this may take a minute.")
df = pd.read_excel(file_path)

print("1. Null Counts Per Column:")
print(df.isnull().sum())

print("\n2. Unique Customer Count:")
unique_customers = df['Customer ID'].nunique()
print(unique_customers)

print("\n3. Negative Quantities (Returns):")
negative_qty = df[df['Quantity'] < 0]
print(len(negative_qty))

print("\n4. Cancelled Orders (Invoices starting with 'C'):")
cancelled_orders = df[df['Invoice'].astype(str).str.startswith('C', na=False)]
print(len(cancelled_orders))