# Project 1: Retail Deep Dive - Presentation Notes

## The Story (5-minute script)

"I worked with the UCI Online Retail II dataset - 400,947 clean 
transactions from a UK e-commerce retailer generating £8.80M in revenue.

I built the full pipeline end-to-end: cleaned the raw data in Python, 
engineered RFM features, loaded it into SQLite for SQL analysis, then 
visualised the findings in a 3-page Power BI dashboard.

The key insight was around customer segmentation - only 460 customers 
(10.67%) are Champions driving disproportionate revenue, while 865 
customers (20%) are Lost and need a win-back strategy.

Peak trading is Thursday at 12pm, which directly informs when a 
marketing team should schedule campaigns."

## Interview Q&A

**Q1: Why did you drop rows without Customer IDs?**
A: Rows without Customer IDs cannot be attributed to any customer 
behaviour. Including them would corrupt the RFM segmentation and 
inflate transaction counts without adding analytical value. 
In a production environment I would flag these as anonymous 
sessions rather than drop them entirely.

**Q2: How would this scale to a larger dataset?**
A: The Python pipeline is fully vectorised using Pandas - no loops. 
For 10M+ rows I would move from SQLite to PostgreSQL or BigQuery, 
and partition the DateTable by year. The Power BI data model uses 
a star schema so it is already optimised for scale.

**Q3: What would you do differently?**
A: I would add cohort retention analysis to track whether Champions 
remain Champions month-on-month. I would also build an automated 
refresh pipeline using Python scheduled via cron so the dashboard 
updates without manual intervention.