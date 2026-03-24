# Project 1: Retail Deep Dive — Project Notes

## Day 31: Initial Data Inspection

### What Was Done

- **Downloaded the dataset** — `online_retail_II.xlsx` (45.6 MB) placed in `data/raw/`.
- **Created project folder structure** — `data/raw/`, `data/cleaned/`, `scripts/`, `sql/`, `powerbi/` all set up inside `retail_deep_dive/`.
- **Loaded the file into Pandas** — used `pd.read_excel()` inside `scripts/data_inspection.py`.
- **Ran `df.info()`** — confirmed 525,461 rows, 8 columns, 32.1+ MB memory usage.
- **Ran `df.describe()`** — confirmed key stats: Quantity min -9,600, Price min -53,594.36, Customer ID has 107,927 missing values.

### Key Findings

- `Customer ID` has **107,927 missing values** — biggest data quality issue.
- `Description` has **2,928 missing values** — minor issue.
- `Quantity` has **negative values** (min -9,600) — indicates returns/cancellations.
- `Price` has **extreme negative values** (min -53,594.36) — likely bad data or credit notes.


## Day 32: Deep Data Profiling

### What Was Done

- **Ran `eda_report.py`** — executed the EDA script on the raw `online_retail_II.xlsx` dataset via VS Code terminal.
- **Investigated null counts per column** — confirmed `Customer ID` and `Description` as the only columns with missing values.
- **Counted unique customers** — used `df['Customer ID'].nunique()` to identify total distinct customers.
- **Identified negative quantities** — filtered `df[df['Quantity'] < 0]` to isolate return transactions.
- **Identified cancelled orders** — filtered invoices starting with `'C'` using `.str.startswith('C')`.

### Key Findings

- `Description` has **2,928 null values** — minor issue, non-critical free text field.
- `Customer ID` has **107,927 null values** — critical issue, these rows must be dropped in cleaning.
- **Unique customers: 4,383** — the active customer base across the full dataset.
- **Negative quantity rows: 12,326** — these are return transactions and must be excluded from sales analysis.
- **Cancelled orders: 10,206** — invoices prefixed with `'C'` representing cancelled transactions to be removed.



## Day 33: Python Data Cleaning

### What Was Done

- **Created `scripts/01_clean.py`** — a structured, documented cleaning script.
- **Dropped null Customer ID rows** — removed 107,927 rows with no customer identifier.
- **Removed duplicate rows** — removed 6,771 exact duplicate records.
- **Removed cancellations** — filtered out invoices prefixed with `'C'`, removing 9,816 rows.
- **Removed negative quantities** — no additional rows removed (already covered by cancellation removal).
- **Parsed `InvoiceDate`** — converted to datetime using `pd.to_datetime()`.
- **Exported cleaned data** — saved to `data/cleaned/retail_cleaned.csv`.

### Key Findings

- **Raw rows: 525,461** — starting point before any cleaning.
- **Final clean rows: 400,947** — 124,514 rows removed in total across all steps.
- **Biggest removal: null Customer ID** — 107,927 rows dropped, confirming Day 32 finding.
- **Duplicates found: 6,771** — would have skewed aggregations if left in.
- **Data is now clean and ready** for SQL analysis and feature engineering in Day 34.

## Day 34: Python Feature Engineering

### What Was Done

- **Created `scripts/02_feature_engineering.py`** — a structured feature engineering and RFM calculation script.
- **Engineered 4 new columns** — Revenue, Month, DayOfWeek, Hour added to the cleaned dataset.
- **Calculated snapshot date** — set as 1 day after the last transaction (2010-12-10) to use as the Recency reference point.
- **Created `Days_Ago` column** — computed days between each transaction and snapshot date before grouping, avoiding complex lambda logic.
- **Computed RFM base metrics** — used `.groupby("Customer ID").agg()` to calculate Recency, Frequency, and Monetary per customer.
- **Exported RFM table** — saved to `data/cleaned/rfm_base.csv`.

### Key Findings

- **4,314 unique customers** in the RFM base — slightly fewer than Day 32 raw count (4,383) due to cleaning.
- **Recency mean: 91 days, median: 53 days** — over half the customer base has not purchased in nearly 2 months, indicating churn risk.
- **Frequency median: 2 orders** — most customers are low-frequency buyers, only 25% have 5+ orders.
- **Monetary median: £700, mean: £2,039** — large gap confirms a small number of high-value customers are pulling the average up.
- **Monetary min: £0.00** — at least one customer has zero total spend, a data quality flag worth monitoring.
- **Top spender: £349,164** — likely a wholesale/B2B account, not a typical retail customer.
## Day 35: Load Cleaned Data into SQLite

### What Was Done

- **Created `scripts/03_load_to_sql.py`** — loaded `retail_cleaned.csv` into SQLite using `df.to_sql()`.
- **Created `data/retail.db`** — SQLite database file saved inside the project.
- **Loaded `transactions` table** — 400,947 rows written successfully.
- **Installed SQLite by alexcvzz** — VS Code extension for running SQL queries directly in editor.
- **Connected `retail.db` in VS Code** — via `Cmd + Shift + P` - `SQLite: Open Database`.
- **Ran sanity check queries** — confirmed row count and column structure in results panel.
- **Created `sql/` folder** — saved first SQL file as `sql/00_sanity_check.sql`.

### Key Findings

- **Rows confirmed: 400,947** — matches cleaned CSV exactly, no data lost in transfer.
- **All 8 columns present** — Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country.
- **Python to SQL handoff complete** — data is now queryable via SQL in VS Code.
- **`sql/` folder established** — all future SQL files saved here, scripts/ for Python only.
