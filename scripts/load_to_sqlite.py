import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# -----------------------
# DIM FUND
# -----------------------

dim_fund = fund_master[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "risk_category"
    ]
]

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------
# FACT NAV
# -----------------------

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------
# FACT TRANSACTIONS
# -----------------------

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------
# FACT PERFORMANCE
# -----------------------

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully!")

# -----------------------
# VERIFY ROW COUNTS
# -----------------------

conn = sqlite3.connect(
    "bluestock_mf.db"
)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )

    print(
        table,
        ":",
        count.iloc[0]["total"]
    )

conn.close()