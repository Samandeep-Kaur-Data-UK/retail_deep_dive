import pandas as pd

# 1. Define where the file is located. 
# We use '../' to tell Python to step out of the 'scripts' folder and go into the 'data/raw' folder.
file_path = 'data/raw/online_retail_II.xlsx'

# 2. Load the Excel file into a Pandas DataFrame
print("Loading data... this is a large file, so it might take a minute.")
df = pd.read_excel(file_path)

# 3. Print out the basic information (columns, missing values, data types)
print("\n--- Data Information ---")
df.info()

# 4. Print out the math summary (averages, minimums, maximums)
print("\n--- Data Summary ---")
print(df.describe())