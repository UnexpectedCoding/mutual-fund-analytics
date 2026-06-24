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