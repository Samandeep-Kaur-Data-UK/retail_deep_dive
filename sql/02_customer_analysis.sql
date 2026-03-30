-- ============================================================
-- Project 1: Retail Deep Dive
-- File: 02_customer_analysis.sql
-- Analyst: Samandeep Kaur
-- Description: Customer Behaviour Analysis using Window Functions
-- Business Application: Customer retention and cohort analysis
--                       KPIs reported at board level in UK retail
-- ============================================================

-- Business Insights:
-- 1. Top customers by revenue = targets for loyalty/retention campaigns
-- 2. Cohort sizes show growth/decline in new customer acquisition
-- 3. Repeat purchase rate % = headline KPI for board-level retention reporting

-- ============================================================
-- QUERY 1: Customer Ranking by Revenue using RANK()
-- ============================================================

SELECT
    "Customer ID",
    ROUND(SUM(Quantity * Price), 2) AS total_revenue,
    RANK() OVER (ORDER BY SUM(Quantity * Price) DESC) AS revenue_rank
FROM transactions
WHERE "Customer ID" IS NOT NULL
  AND Quantity > 0
  AND Price > 0
GROUP BY "Customer ID"
ORDER BY revenue_rank;

-- ============================================================
-- QUERY 2: Monthly Cohort Size (New Customers Per Month)
-- ============================================================

SELECT
    strftime('%Y-%m', first_purchase) AS cohort_month,
    COUNT("Customer ID") AS new_customers
FROM (
    SELECT
        "Customer ID",
        MIN(InvoiceDate) AS first_purchase
    FROM transactions
    WHERE "Customer ID" IS NOT NULL
    GROUP BY "Customer ID"
) AS first_orders
GROUP BY cohort_month
ORDER BY cohort_month;

-- ============================================================
-- QUERY 3: Repeat Purchase Rate
-- ============================================================

SELECT
    ROUND(
        100.0 * COUNT(CASE WHEN purchase_count > 1 THEN 1 END) / COUNT(*),
        2
    ) AS repeat_purchase_rate_pct
FROM (
    SELECT
        "Customer ID",
        COUNT(DISTINCT Invoice) AS purchase_count
    FROM transactions
    WHERE "Customer ID" IS NOT NULL
    GROUP BY "Customer ID"
) AS customer_orders;