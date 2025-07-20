import os
import pandas as pd
from datetime import datetime

# Set base directories
base_dir = r"C:\Users\rites\Downloads\sample_data_project\data"
output_dir = r"C:\Users\rites\Downloads\sample_data_project\output"
os.makedirs(output_dir, exist_ok=True)

# Helper to convert date from filename
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")

# Process CUST_MSTR files
cust_path = os.path.join(base_dir, "CUST_MSTR")
cust_frames = []
for file in os.listdir(cust_path):
    if file.startswith("CUST_MSTR"):
        date_str = file.split("_")[2].split(".")[0]
        full_date = parse_date(date_str)
        df = pd.read_csv(os.path.join(cust_path, file))
        df['Date'] = full_date
        cust_frames.append(df)
pd.concat(cust_frames).to_csv(os.path.join(output_dir, "CUST_MSTR_cleaned.csv"), index=False)

# Process master_child_export files
mc_path = os.path.join(base_dir, "master_child_export")
mc_frames = []
for file in os.listdir(mc_path):
    if file.startswith("master_child_export"):
        date_str = file.split("-")[1].split(".")[0]
        full_date = parse_date(date_str)
        df = pd.read_csv(os.path.join(mc_path, file))
        df['Date'] = full_date
        df['DateKey'] = int(date_str)
        mc_frames.append(df)
pd.concat(mc_frames).to_csv(os.path.join(output_dir, "master_child_cleaned.csv"), index=False)

# Process H_ECOM_ORDER files
ecom_path = os.path.join(base_dir, "H_ECOM_ORDER")
for file in os.listdir(ecom_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(ecom_path, file))
        df.to_csv(os.path.join(output_dir, "H_ECOM_ORDER_cleaned.csv"), index=False)

print("✅ ETL completed! Cleaned files saved to 'output' folder.")

