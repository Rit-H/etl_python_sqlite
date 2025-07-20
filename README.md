# 🧪 Python ETL Pipeline – Local Simulation of Azure Data Lake to SQL

This project simulates an Azure Data Factory ETL pipeline using **Python** and **SQLite** locally. It reads CSV files from different folders, extracts date info from filenames, adds necessary columns, and loads data into a local SQLite database.

## 📁 Folder Structure


## 📦 Files

- `CUST_MSTR_YYYYMMDD.csv` → Adds `Date` column from filename
- `master_child_export-YYYYMMDD.csv` → Adds `Date` and `DateKey`
- `H_ECOM_ORDER.csv` → Loaded as-is

## ✅ Features

- Simulates truncate-load pipeline
- Merges multiple CSVs
- Adds derived columns using filename
- Loads data to SQLite using Pandas

## 💡 To Run

```bash
# Step 1: Run ETL
python etl_script.py

# Step 2: Load cleaned data into SQLite
python load_to_sqlite.py
