import duckdb

conn = duckdb.connect("warehouse.db")

result = conn.execute("SELECT * FROM dim_products LIMIT 5").fetchdf()

print(result)