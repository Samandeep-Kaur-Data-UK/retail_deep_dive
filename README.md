# Retail Deep Dive | UK E-Commerce Analytics
Portfolio-ready retail analytics project using Python, SQL, and Power BI to turn transaction data into customer, revenue, and trading insights.
**Tech Stack:** Python, Pandas, SQLite, SQL, Power BI

## Project Overview
This project uses the UCI Online Retail II dataset to answer the kind of questions a UK retail team would ask in a weekly or monthly trading review:

- Which products, countries, and periods drive the most revenue?
- Which customers are highest value and which are at risk?
- When should a retailer time campaigns to capture the strongest demand?

The workflow covers the full analytics pipeline: raw data inspection, Python cleaning, feature engineering, SQL analysis, RFM segmentation, and a 3-page Power BI dashboard.

## Dataset
- Source: [UCI Online Retail II Dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- Raw dataset size: 525,461 rows
- Clean dataset size: 400,947 transactions
- Coverage: December 2009 to December 2010

## Workflow
1. Cleaned the raw Excel dataset in Python by removing missing customer IDs, duplicate rows, cancellations, and invalid negative transactions.
2. Engineered revenue and time-based features plus an RFM base table for customer analysis.
3. Loaded the cleaned data into SQLite and answered revenue, cohort, and segmentation questions with SQL.
4. Built a Power BI report with executive, customer, and trend-analysis views for stakeholder review.

## Key Results
| Metric | Value |
|--------|-------|
| Total Revenue | £8.80M |
| Total Orders | 19,215 |
| Average Order Value | £457.88 |
| Total Customers | 4,314 |
| Champions (RFM) | 460 customers |
| Champions Share | 10.67% |
| Repeat Purchase Rate | 67.06% |
| Peak Revenue Month | November 2010 (£1.17M) |
| Peak Trading Day | Thursday |
| Peak Trading Hour | 12pm |
| Top International Market | EIRE (£356k) |

## Business Recommendations
- Prioritise retention and CRM campaigns around the 460 Champion customers who drive disproportionate value.
- Build win-back activity for lower-value and at-risk segments before they move into churn.
- Time promotional pushes around Thursday midday, the strongest revenue window in the dataset.
- Use EIRE as the clearest international expansion benchmark outside the UK market.

## Dashboard Preview
### Executive Summary
![Executive Summary](screenshots/executive_summary.png)

### Customer Intelligence
![Customer Intelligence](screenshots/customer_intelligence.png)

### Trend Analysis
![Trend Analysis](screenshots/trend_analysis.png)

## Files To Review First
- `README.md` for the project summary and outcome metrics
- `project_notes.md` for the day-by-day analytical build and findings
- `presentation_notes.md` for the interview walkthrough
- `sql/01_revenue_analysis.sql`, `sql/02_customer_analysis.sql`, and `sql/03_rfm_segmentation.sql` for the SQL work
- `powerbi/Retail_DD_Day43_ReportPolish_Final.pbix` for the final dashboard

## Project Structure
```text
retail_deep_dive/
|-- data/
|   |-- raw/online_retail_II.xlsx
|   |-- cleaned/retail_cleaned.csv
|   |-- cleaned/retail_enriched.csv
|   |-- cleaned/rfm_base.csv
|   |-- cleaned/rfm_segments.csv
|   `-- retail.db
|-- scripts/
|   |-- 01_clean.py
|   |-- 02_feature_engineering.py
|   |-- 03_load_to_sql.py
|   |-- data_inspection.py
|   `-- eda_report.py
|-- sql/
|   |-- 00_sanity_check.sql
|   |-- 01_revenue_analysis.sql
|   |-- 02_customer_analysis.sql
|   `-- 03_rfm_segmentation.sql
|-- powerbi/
|   `-- Retail_DD_Day43_ReportPolish_Final.pbix
|-- screenshots/
|   |-- executive_summary.png
|   |-- customer_intelligence.png
|   `-- trend_analysis.png
|-- presentation_notes.md
|-- project_notes.md
`-- requirements.txt
```

## How To Run
From the project root:

```bash
pip install -r requirements.txt
python scripts/01_clean.py
python scripts/02_feature_engineering.py
python scripts/03_load_to_sql.py
```

To inspect the final dashboard, open:

```text
powerbi/Retail_DD_Day43_ReportPolish_Final.pbix
```
