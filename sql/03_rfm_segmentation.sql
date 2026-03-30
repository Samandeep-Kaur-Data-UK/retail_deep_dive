-- ============================================================
-- Project 1: Retail Deep Dive
-- File: 03_rfm_segmentation.sql
-- Analyst: Samandeep Kaur
-- Description: RFM Segmentation using CTEs
-- Business Application: Feeds CRM, email marketing, and
--                       retention budget decisions
-- ============================================================

-- ============================================================
-- CTE 1: Calculate Raw RFM Metrics Per Customer
-- ============================================================

WITH rfm_base AS (
    SELECT
        "Customer ID",
        CAST(julianday('2010-12-10') - julianday(MAX(InvoiceDate)) AS INTEGER) AS recency_days,
        COUNT(DISTINCT Invoice) AS frequency,
        ROUND(SUM(Quantity * Price), 2) AS monetary
    FROM transactions
    WHERE "Customer ID" IS NOT NULL
      AND Quantity > 0
      AND Price > 0
    GROUP BY "Customer ID"
),

-- ============================================================
-- CTE 2: Score Each Metric 1-4 Using NTILE(4)
-- ============================================================

rfm_scores AS (
    SELECT
        "Customer ID",
        recency_days,
        frequency,
        monetary,
        NTILE(4) OVER (ORDER BY recency_days ASC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency DESC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary DESC) AS m_score
    FROM rfm_base
),

-- ============================================================
-- CTE 3: Combine Scores into Segment Labels
-- ============================================================

rfm_segments AS (
    SELECT
        "Customer ID",
        recency_days,
        frequency,
        monetary,
        r_score,
        f_score,
        m_score,
        (r_score + f_score + m_score) AS total_score,
        CASE
            WHEN r_score = 4 AND f_score = 4 AND m_score = 4 THEN 'Champions'
            WHEN r_score >= 3 AND f_score >= 3 THEN 'Loyal Customers'
            WHEN r_score >= 3 AND f_score <= 2 THEN 'Potential Loyalists'
            WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk'
            WHEN r_score = 1 AND f_score = 1 THEN 'Lost'
            ELSE 'Needs Attention'
        END AS segment
    FROM rfm_scores
)

-- ============================================================
-- FINAL: Output Full Segmented Customer Table
-- ============================================================

SELECT *
FROM rfm_segments
ORDER BY total_score DESC;