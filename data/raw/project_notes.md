## Day 31: Initial Data Inspection

### What Was Done

* **Downloaded the dataset**: `online_retail_II.xlsx` (45.6 MB) placed in `data/raw/`.
* **Created project folder structure**: `data/raw/`, `data/cleaned/`, `scripts/`, `sql/`, `powerbi/` all set up inside `retail_deep_dive/`.
* **Loaded the file into Pandas**: used `pd.read_excel()` inside `scripts/data_inspection.py`.
* **Ran `df.info()`**: confirmed 525,461 rows, 8 columns, 32.1+ MB memory usage.
* **Ran `df.describe()`**: confirmed key stats: Quantity min -9,600, Price min -53,594.36, Customer ID has 107,927 missing values.

### Key Findings

* `Customer ID` has **107,927 missing values**: biggest data quality issue.
* `Description` has **2,928 missing values**: minor issue.
* `Quantity` has **negative values** (min -9,600): indicates returns/cancellations.
* `Price` has **extreme negative values** (min -53,594.36): likely bad data or credit notes.


## Day 32: Deep Data Profiling

### What Was Done

* **Ran `eda_report.py`**: executed the EDA script on the raw `online_retail_II.xlsx` dataset via VS Code terminal.
* **Investigated null counts per column**: confirmed `Customer ID` and `Description` as the only columns with missing values.
* **Counted unique customers**: used `df['Customer ID'].nunique()` to identify total distinct customers.
* **Identified negative quantities**: filtered `df[df['Quantity'] < 0]` to isolate return transactions.
* **Identified cancelled orders**: filtered invoices starting with `'C'` using `.str.startswith('C')`.

### Key Findings

* `Description` has **2,928 null values**: minor issue, non-critical free text field.
* `Customer ID` has **107,927 null values**: critical issue, these rows must be dropped in cleaning.
* **Unique customers: 4,383**: the active customer base across the full dataset.
* **Negative quantity rows: 12,326**: these are return transactions and must be excluded from sales analysis.
* **Cancelled orders: 10,206**: invoices prefixed with `'C'` representing cancelled transactions to be removed.


## Day 33: Python Data Cleaning

### What Was Done

* **Created `scripts/01_clean.py`**: a structured, documented cleaning script.
* **Dropped null Customer ID rows**: removed 107,927 rows with no customer identifier.
* **Removed duplicate rows**: removed 6,771 exact duplicate records.
* **Removed cancellations**: filtered out invoices prefixed with `'C'`, removing 9,816 rows.
* **Removed negative quantities**: no additional rows removed (already covered by cancellation removal).
* **Parsed `InvoiceDate`**: converted to datetime using `pd.to_datetime()`.
* **Exported cleaned data**: saved to `data/cleaned/retail_cleaned.csv`.

### Key Findings

* **Raw rows: 525,461**: starting point before any cleaning.
* **Final clean rows: 400,947**: 124,514 rows removed in total across all steps.
* **Biggest removal: null Customer ID**: 107,927 rows dropped, confirming Day 32 finding.
* **Duplicates found: 6,771**: would have skewed aggregations if left in.
* **Data is now clean and ready** for SQL analysis and feature engineering in Day 34.


## Day 34: Python Feature Engineering

### What Was Done

* **Created `scripts/02_feature_engineering.py`**: a structured feature engineering and RFM calculation script.
* **Engineered 4 new columns**: Revenue, Month, DayOfWeek, Hour added to the cleaned dataset.
* **Calculated snapshot date**: set as 1 day after the last transaction (2010-12-10) to use as the Recency reference point.
* **Created `Days_Ago` column**: computed days between each transaction and snapshot date before grouping, avoiding complex lambda logic.
* **Computed RFM base metrics**: used `.groupby("Customer ID").agg()` to calculate Recency, Frequency, and Monetary per customer.
* **Exported RFM table**: saved to `data/cleaned/rfm_base.csv`.

### Key Findings

* **4,314 unique customers** in the RFM base: slightly fewer than Day 32 raw count (4,383) due to cleaning.
* **Recency mean: 91 days, median: 53 days**: over half the customer base has not purchased in nearly 2 months, indicating churn risk.
* **Frequency median: 2 orders**: most customers are low-frequency buyers, only 25% have 5+ orders.
* **Monetary median: £700, mean: £2,039**: large gap confirms a small number of high-value customers are pulling the average up.
* **Monetary min: £0.00**: at least one customer has zero total spend, a data quality flag worth monitoring.
* **Top spender: £349,164**: likely a wholesale/B2B account, not a typical retail customer.


## Day 35: Load Cleaned Data into SQLite

### What Was Done

* **Created `scripts/03_load_to_sql.py`**: loaded `retail_cleaned.csv` into SQLite using `df.to_sql()`.
* **Created `data/retail.db`**: SQLite database file saved inside the project.
* **Loaded `transactions` table**: 400,947 rows written successfully.
* **Installed SQLite by alexcvzz**: VS Code extension for running SQL queries directly in editor.
* **Connected `retail.db` in VS Code**: via `Cmd + Shift + P` -> `SQLite: Open Database`.
* **Ran sanity check queries**: confirmed row count and column structure in results panel.
* **Created `sql/` folder**: saved first SQL file as `sql/00_sanity_check.sql`.

### Key Findings

* **Rows confirmed: 400,947**: matches cleaned CSV exactly, no data lost in transfer.
* **All 8 columns present**: Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country.
* **Python to SQL handoff complete**: data is now queryable via SQL in VS Code.
* **`sql/` folder established**: all future SQL files saved here, scripts/ for Python only.


## Day 36: SQL Analysis, Revenue and Sales Performance

### What Was Done

* **Created `sql/01_revenue_analysis.sql`**: set up the first analytical SQL script.
* **Calculated Total Revenue by Month**: used `strftime('%Y-%m', InvoiceDate)` to group revenue chronologically.
* **Identified Top 10 Products**: grouped by `Description` to find primary volume drivers.
* **Identified Top 10 International Markets**: filtered out 'United Kingdom' to analyze global reach.
* **Calculated Average Order Value (AOV)**: divided total revenue by the distinct count of `Invoice`.
* **Troubleshooted Column Names**: successfully identified the exact schema (`Price` and `Invoice`) in SQLite to execute queries.

### Key Findings

* **Monthly Trend**: The highest revenue was generated in [Insert Month].
* **Top Product**: Our primary volume driver is [Insert Product Name], generating £[Insert Revenue].
* **International Market**: Excluding the UK, our biggest expansion opportunity is in [Insert Country].



## Day 37: SQL Analysis, Customer Behaviour with Window Functions

### What Was Done

* **Created `sql/02_customer_analysis.sql`**: set up the second analytical SQL script focused on customer behaviour.
* **Debugged table loading issue**: `retail.db` existed but was empty - loaded `retail_cleaned.csv` into SQLite via Python `df.to_sql()` to create the `transactions` table.
* **Fixed column name mismatch**: actual columns confirmed as `Invoice`, `Price`, `Customer ID` (with space) - updated all queries accordingly using double quotes around `"Customer ID"`.
* **Query 1 - Customer Ranking by Revenue**: used `RANK()` window function ordered by `SUM(Quantity * Price) DESC` to rank all 4,312 customers by total spend.
* **Query 2 - Monthly Cohort Size**: used `MIN(InvoiceDate)` inside a subquery to find each customer's first purchase date, then grouped by `strftime('%Y-%m')` to count new customers per month.
* **Query 3 - Repeat Purchase Rate**: used `COUNT(DISTINCT Invoice)` per customer inside a subquery, then applied `CASE WHEN purchase_count > 1` to calculate the percentage of returning customers.

### Key Findings

* **Top customer (18102)**: total spend of £349,164.35 - likely a wholesale or B2B account.
* **4,312 unique customers ranked**: confirms active customer base post-cleaning.
* **Largest new customer cohort**: December 2009 with 955 new customers.
* **13 monthly cohorts total**: dataset spans December 2009 to December 2010.
* **Repeat purchase rate: 67.06%**: 2 in 3 customers returned to buy again - strong retention signal for board-level reporting.


## Day 38: SQL Analysis, RFM Segmentation with CTEs

### What Was Done

* **Created `03_rfm_segmentation.sql`**: set up the third analytical SQL script focused on RFM (Recency, Frequency, Monetary) segmentation for CRM and marketing applications.
* **Built Raw Metrics (CTE 1)**: used `julianday()` to calculate recency days from a fixed date ('2010-12-10'), `COUNT(DISTINCT Invoice)` for frequency, and `SUM(Quantity * Price)` for monetary value.
* **Applied Quartile Scoring (CTE 2)**: utilized the `NTILE(4)` window function to rank and divide the customer base into quartiles (1 to 4) across all three RFM dimensions.
* **Defined Customer Segments (CTE 3)**: implemented a `CASE WHEN` statement to categorize customers into actionable business segments like 'Champions', 'Loyal Customers', and 'At Risk' based on their combined `r_score`, `f_score`, and `m_score`.

### Key Findings

* **Actionable Segmentation**: successfully categorized the active customer base into 6 distinct tiers, ranging from highly valuable 'Champions' to 'Lost' accounts.
* **CRM Readiness**: the final output maps every `Customer ID` directly to a segment label and `total_score`, making the dataset immediately ready for targeted email marketing and retention campaigns.
* **Data Quality Enforced**: the base CTE successfully filtered out negative quantities and prices (Quantity > 0, Price > 0), ensuring only valid, revenue-generating transactions influenced the final RFM scores.


