import pandas as pd

# Load the data using your existing Mac path
file_path = '/Users/samandeep/Downloads/online_retail.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

print("1. Null Counts Per Column:")
print(df.isnull().sum())

print("\n2. Unique Customer Count:")
unique_customers = df['CustomerID'].nunique()
print(unique_customers)

print("\n3. Negative Quantities (Returns):")
negative_qty = df[df['Quantity'] < 0]
print(len(negative_qty))

print("\n4. Cancelled Orders (Invoices starting with 'C'):")
cancelled_orders = df[df['InvoiceNo'].astype(str).str.startswith('C', na=False)]
print(len(cancelled_orders))