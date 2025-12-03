import pandas as pd


# 1) Load the raw data (same path you used in extract.py)
file_path = r"C:\Users\namra\company_data_pipeline\data\raw\Top 2000 Companies Financial Data 2024.csv"
df = pd.read_csv(file_path)


# 2) Rename and select columns for the final schema
df = df.rename(columns={
    "Name": "company_name",
    "Country": "country",
    "Sales": "revenue",
    "Profit": "profit",
    "Assets": "assets",
    "Market Value": "market_value"
})


# Keep only the columns you need
df = df[["company_name", "country", "revenue", "profit", "assets", "market_value"]]


# 3) Add required extra columns
df["year"] = 2024
df["revenue_unit"] = "USD Billion"
df["industry"] = ""   # dataset doesn’t have industry – leave empty and explain in README


# 4) Clean currency strings to numeric (remove $, commas, B)
currency_cols = ["revenue", "profit", "assets", "market_value"]
for col in currency_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(" B", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")


# 5) Drop rows with missing critical fields
df = df.dropna(subset=["company_name", "country", "revenue"])


# 6) Ensure 100–500 unique companies (sample 300 here)
df = df.drop_duplicates(subset=["company_name"])
df = df.sample(n=300, random_state=42)  # you can change 300 to any number 100–500


# 7) Reorder columns nicely
df = df[[
    "company_name",
    "country",
    "industry",
    "year",
    "revenue",
    "revenue_unit",
    "profit",
    "assets",
    "market_value"
]]


# 8) Save the final cleaned dataset
output_path = r"C:\Users\namra\company_data_pipeline\data\processed\companies_financials_clean.csv"
df.to_csv(output_path, index=False)


print("Saved cleaned data to", output_path)
print("Number of companies:", df["company_name"].nunique())
