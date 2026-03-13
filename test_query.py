import duckdb

conn = duckdb.connect("warehouse.db")

result = conn.execute("SELECT * FROM raw_products LIMIT 5").fetchdf()

print(result)