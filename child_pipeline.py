
import sys
import sqlite3
import pandas as pd

# Get customer count from parent
customer_count = int(sys.argv[1])
print(f"🔄 Received customer count: {customer_count}")

if customer_count > 600:
    conn = sqlite3.connect("customer_data.db")
    df = pd.read_sql("SELECT * FROM Product", conn)
    df.to_csv("output_product.csv", index=False)
    conn.close()
    print("✅ Product data copied to output_product.csv")
else:
    print("❌ Skipped: Customer count not greater than 600")
