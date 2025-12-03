# Company Financials Data Pipeline

## Project goal

This project implements a small ETL / data-engineering pipeline.  
It extracts a public dataset with global companies, cleans and transforms the data with Python, and produces a structured CSV containing 300 companies and key financial KPIs. [attached_file:246]

## Data source

- Dataset: Top 2000 Companies Financial Data 2024 (Forbes Global 2000 2024, Kaggle) [web:44]  
- Content: Company name, country, sales (revenue), profit, assets, market value for about 2,000 companies for the year 2024. [web:44]

The dataset is stored locally in:

- `data/raw/Top 2000 Companies Financial Data 2024.csv`

## Pipeline steps

### 1. Extraction (`src/extract.py`)

- Loads the raw CSV from `data/raw`.  
- Prints `head()`, `columns`, and `info()` to understand structure and data types. [web:151]  

### 2. Transformation (`src/transform.py`)

Main operations: [web:232][web:237]

- Rename columns:
  - `Name` → `company_name`
  - `Country` → `country`
  - `Sales` → `revenue`
  - `Profit` → `profit`
  - `Assets` → `assets`
  - `Market Value` → `market_value`
- Keep only needed columns, then add:
  - `year = 2024`
  - `revenue_unit = "USD Billion"`
  - `industry` (empty, because the source dataset does not include industry) [attached_file:246]
- Clean currency strings (`revenue`, `profit`, `assets`, `market_value`):
  - Remove `$`, commas, and the suffix `B`, then convert to numeric.
- Drop rows with missing `company_name`, `country`, or `revenue`.  
- Ensure between 100 and 500 companies:
  - Drop duplicate company names.
  - Sample 300 companies with `random_state=42`. [web:237]
- Save the final dataset to:
  - `data/processed/companies_financials_clean.csv`

## Final dataset schema

Each row represents one company in 2024. Columns: [attached_file:246]

- `company_name`: Name of the company.  
- `country`: Country of the company’s main headquarters.  
- `industry`: Empty for now (not available in the source; could be added from another reference dataset).  
- `year`: Financial year (2024).  
- `revenue`: Company sales / revenue (numeric, billions).  
- `revenue_unit`: Unit of `revenue` (string), here `"USD Billion"`.  
- `profit`: Profit (numeric, USD billions).  
- `assets`: Total assets (numeric, USD billions).  
- `market_value`: Market value (numeric, USD billions).

## Notes and limitations

- Industry information is not provided in the source dataset, so the `industry` column is left empty and documented here. [attached_file:246]  
- The case study asks for up to 3 most recent years “if available”. This public dataset only contains 2024 data, so only one year per company is included. [attached_file:246]

## How to run

Requirements: [web:151]

- Python 3.11
- `pandas` (`pip install pandas`)

Steps:

