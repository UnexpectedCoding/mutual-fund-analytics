# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Scheme Name |
| category | Text | Equity/Debt |
| sub_category | Text | Fund Category |
| plan | Text | Direct/Regular |
| launch_date | Date | Scheme Launch Date |
| benchmark | Text | Benchmark Index |
| expense_ratio_pct | Float | Expense Ratio Percentage |
| exit_load_pct | Float | Exit Load Percentage |
| fund_manager | Text | Fund Manager |
| risk_category | Text | Risk Classification |

---

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | 1-Year Return |
| return_3yr_pct | Float | 3-Year Return |
| return_5yr_pct | Float | 5-Year Return |
| alpha | Float | Alpha |
| beta | Float | Beta |
| sharpe_ratio | Float | Sharpe Ratio |
| expense_ratio_pct | Float | Expense Ratio |
| aum_crore | Float | Assets Under Management |

---

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Unique Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| kyc_status | Text | KYC Verification Status |

Source:
- AMFI India
- MFAPI NAV Data