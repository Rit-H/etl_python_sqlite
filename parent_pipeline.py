
import sqlite3
import subprocess
import pandas as pd

# Connect to database
conn = sqlite3.connect("customer_data.db")
cursor = conn.cursor()

# Get customer count
cursor.execute("SELECT COUNT(*) FROM Customer")
count = cursor.fetchone()[0]
print(f"📊 Customer count: {count}")

# If count > 500, copy and trigger child pipeline
if count > 500:
    df = pd.read_sql("SELECT * FROM Customer", conn)
    df.to_csv("output_customer.csv", index=False)
    print("✅ Customer data copied to output_customer.csv")
    subprocess.run(["python", "child_pipeline.py", str(count)])
else:
    print("❌ Skipped: Customer count is below 500")

conn.close()
