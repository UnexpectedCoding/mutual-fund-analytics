import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

csv_files = list(RAW_PATH.glob("*.csv"))

print("="*80)
print(f"Found {len(csv_files)} CSV files")
print("="*80)

for file in csv_files:

    print("\n")
    print("="*80)
    print(f"FILE: {file.name}")
    print("="*80)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"ERROR: {e}")
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

csv_files = list(RAW_PATH.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "="*50)
    print(file.name)
    print("="*50)

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")
print("="*60)
print("FUND MASTER ANALYSIS")
print("="*60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\n")
print("="*60)
print("AMFI CODE VALIDATION")
print("="*60)


# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

nav_history = pd.read_csv("data/raw/02_nav_history.csv")


# Extract AMFI codes
master_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])


# Find missing codes
missing_codes = master_codes - nav_codes


# Print results
print("\nTotal Fund Master AMFI Codes:")
print(len(master_codes))


print("\nTotal NAV History AMFI Codes:")
print(len(nav_codes))


print("\nMissing AMFI Codes:")
print(len(missing_codes))


if len(missing_codes) > 0:
    print("\nMissing Codes List:")
    print(missing_codes)

else:
    print("\nSUCCESS ")
    print("All Fund Master AMFI codes exist in NAV History")