import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)


# NAV HISTORY CLEANING


nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    PROCESSED / "02_nav_history_clean.csv",
    index=False
)

print("NAV History cleaned")


# INVESTOR TRANSACTIONS CLEANING


txn = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_txn = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"]
    .isin(valid_txn)
]

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"]
    .isin(valid_kyc)
]

txn.to_csv(
    PROCESSED /
    "08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions cleaned")


# SCHEME PERFORMANCE CLEANING

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    "\nExpense Ratio Anomalies:",
    len(anomalies)
)

perf.to_csv(
    PROCESSED /
    "07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned")

# ====================================
# FUND MASTER CLEANING
# ====================================

fund = pd.read_csv(RAW / "01_fund_master.csv")

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund = fund.drop_duplicates()

fund.to_csv(
    PROCESSED / "01_fund_master_clean.csv",
    index=False
)

print("Fund Master cleaned")


# ====================================
# AUM BY FUND HOUSE
# ====================================

aum = pd.read_csv(
    RAW / "03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"]
)

aum = aum.drop_duplicates()

aum.to_csv(
    PROCESSED / "03_aum_by_fund_house_clean.csv",
    index=False
)

print("AUM by Fund House cleaned")


# ====================================
# MONTHLY SIP INFLOWS
# ====================================

sip = pd.read_csv(
    RAW / "04_monthly_sip_inflows.csv"
)

sip["month"] = pd.to_datetime(
    sip["month"]
)

sip = sip.drop_duplicates()

sip.to_csv(
    PROCESSED / "04_monthly_sip_inflows_clean.csv",
    index=False
)

print("Monthly SIP Inflows cleaned")


# ====================================
# CATEGORY INFLOWS
# ====================================

cat = pd.read_csv(
    RAW / "05_category_inflows.csv"
)

cat["month"] = pd.to_datetime(
    cat["month"]
)

cat = cat.drop_duplicates()

cat.to_csv(
    PROCESSED / "05_category_inflows_clean.csv",
    index=False
)

print("Category Inflows cleaned")


# ====================================
# INDUSTRY FOLIO COUNT
# ====================================

folio = pd.read_csv(
    RAW / "06_industry_folio_count.csv"
)

folio["month"] = pd.to_datetime(
    folio["month"]
)

folio = folio.drop_duplicates()

folio.to_csv(
    PROCESSED / "06_industry_folio_count_clean.csv",
    index=False
)

print("Industry Folio Count cleaned")


# ====================================
# PORTFOLIO HOLDINGS
# ====================================

holdings = pd.read_csv(
    RAW / "09_portfolio_holdings.csv"
)

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"]
)

holdings = holdings.drop_duplicates()

holdings.to_csv(
    PROCESSED / "09_portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio Holdings cleaned")


# ====================================
# BENCHMARK INDICES
# ====================================

benchmark = pd.read_csv(
    RAW / "10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    PROCESSED / "10_benchmark_indices_clean.csv",
    index=False
)

print("Benchmark Indices cleaned")