# 🧪 ETL Pipeline Project with REST API, SQLite, and Conditional Logic

This project simulates a real-world ETL pipeline using **Python** that:

- Fetches data from a public REST API and stores it in JSON format
- Loads customer and product data from a simulated database
- Applies conditional logic to control data copying and pipeline triggers

---

## 📦 Features

### ✅ Step 1: Country Data via REST API
- Uses `https://restcountries.com` to fetch data for:
  `India`, `US`, `UK`, `China`, and `Russia`
- Saves each country’s data as a separate JSON file

### ✅ Step 2: Conditional ETL with SQLite
- Simulates a database using `SQLite`
- **Parent Pipeline:**
  - Checks customer count
  - Copies to CSV only if count > 500
  - Triggers a child pipeline
- **Child Pipeline:**
  - Receives customer count as a parameter
  - Copies product data only if count > 600

---

## 🗂️ Folder Structure
