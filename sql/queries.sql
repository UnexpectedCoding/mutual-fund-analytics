-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Total SIP Amount

SELECT
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type='Sip';


-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 6. Average Return by Category

SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;


-- 7. Top 5 Funds by 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 8. KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;


-- 9. Total Redemption Amount

SELECT
    SUM(amount_inr) AS redemption_amount
FROM fact_transactions
WHERE transaction_type='Redemption';


-- 10. Fund Count by Fund House

SELECT
    fund_house,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY fund_house
ORDER BY fund_count DESC;