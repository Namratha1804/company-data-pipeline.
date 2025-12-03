import pandas as pd

# Path is from the location of this file (src) to data/raw
file_path = "../data/raw/Top 2000 Companies Financial Data 2024.csv"

df = pd.read_csv(file_path)

print(df.head())
print(df.columns)
print(df.info())
