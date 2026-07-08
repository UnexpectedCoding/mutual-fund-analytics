import pandas as pd

funds = pd.read_csv("reports/fund_scorecard.csv")

risk_map = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Very High", "Moderately High"]
}

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

levels = risk_map.get(risk)

if levels is None:
    print("Invalid Risk Appetite")
else:
    result = funds[
        funds["risk_category"].isin(levels)
    ].sort_values(
        "Sharpe_Ratio",
        ascending=False
    )

    print(result[[
        "scheme_name",
        "risk_category",
        "Sharpe_Ratio"
    ]].head(3))