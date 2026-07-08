import pandas as pd

files = [
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "="*60)
    print(file)
    print("="*60)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())