import duckdb
import pandas as pd

# connect to warehouse database
conn = duckdb.connect("warehouse.db")

print("Connected to DuckDB")

# load orders data
orders_df = pd.read_json("data/raw/orders/orders.json")

conn.execute("CREATE TABLE IF NOT EXISTS raw_orders AS SELECT * FROM orders_df")

print("Orders table created")

# load products data
products_df = pd.read_json("data/raw/products/products.json")

conn.execute("CREATE TABLE IF NOT EXISTS raw_products AS SELECT * FROM products_df")

print("Products table created")

# load customers data
customers_df = pd.read_json("data/raw/customers/customers.json")

conn.execute("CREATE TABLE IF NOT EXISTS raw_customers AS SELECT * FROM customers_df")

print("Customers table created")

print("All raw tables loaded successfully!")