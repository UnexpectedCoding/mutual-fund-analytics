import requests
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

SCHEMES = {
    "HDFC Top 100 Direct": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

for scheme_name, scheme_code in SCHEMES.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Fetching {scheme_name}")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed: {scheme_code}")
        continue

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = scheme_name.lower().replace(" ", "_")
    filepath = RAW_PATH / f"{filename}_nav.csv"

    nav_df.to_csv(filepath, index=False)

    print(f"Saved: {filepath}")