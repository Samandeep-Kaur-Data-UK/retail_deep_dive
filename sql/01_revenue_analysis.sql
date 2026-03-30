/* 1. Total Revenue by Month */
/* This helps identify seasonal trends in the retail data */
SELECT 
    strftime('%Y-%m', InvoiceDate) AS Month, 
    SUM(Quantity * Price) AS Total_Revenue
FROM transactions
GROUP BY Month
ORDER BY Month;

/* 2. Top 10 Products by Revenue */
/* Identifying the highest value drivers */
SELECT 
    Description, 
    SUM(Quantity * Price) AS Product_Revenue
FROM transactions
GROUP BY Description
ORDER BY Product_Revenue DESC
LIMIT 10;

/* 3. Top 10 Countries by Revenue (Excluding UK) */
/* Analyzing international market performance */
SELECT 
    Country, 
    SUM(Quantity * Price) AS International_Revenue
FROM transactions
WHERE Country != 'United Kingdom'
GROUP BY Country
ORDER BY International_Revenue DESC
LIMIT 10;

/* 4. Average Order Value (AOV) */
/* Calculating the mean spend per transaction */
SELECT 
    SUM(Quantity * Price) / COUNT(DISTINCT Invoice) AS Average_Order_Value
FROM transactions;