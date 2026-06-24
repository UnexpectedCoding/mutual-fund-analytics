import pandas as pd

files = [
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
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