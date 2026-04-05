# Retail Deep Dive | UK E-Commerce Analytics

## Project Overview
End-to-end analytics project using the UCI Online Retail II dataset. 
Data cleaned in Python, analysed in SQL, and visualised in Power BI 
to surface commercial insights for a UK-based e-commerce retailer.

## Dataset Source
[UCI Online Retail II Dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- 400,947 clean transactions
- Period: Dec 2009 - Dec 2010

## Tech Stack
- Python 3.14 + Pandas 3.0 (cleaning + feature engineering)
- SQLite + SQL (RFM segmentation, window functions, CTEs)
- Power BI (3-page interactive dashboard)

## Project Structure

## Key Findings
| Metric | Value |
|--------|-------|
| Total Revenue | £8.80M |
| Total Customers | 4,314 |
| Average Order Value | £457.88 |
| Total Orders | 19K |
| Champions (RFM) | 460 (10.67%) |
| Repeat Purchase Rate | 67% |
| Revenue YoY Growth | 11.87% |
| Peak Day | Thursday |
| Peak Hour | 12pm |

## Dashboard Pages
![Executive Summary](screenshots/executive_summary.png)
![Customer Intelligence](screenshots/customer_intelligence.png)
![Trend Analysis](screenshots/trend_analysis.png)

## How to Run
```bash
# 1. Clean data
python scripts/01_clean.py

# 2. Feature engineering
python scripts/02_feature_engineering.py

# 3. Load to SQLite
python scripts/03_load_to_sql.py

# 4. Open Power BI file
# powerbi/Retail_Deep_Dive_Final.pbix
```