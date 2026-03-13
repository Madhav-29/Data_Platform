import requests
import pandas as pd
import os

url = "https://fakestoreapi.com/users"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

os.makedirs("data/raw/customers", exist_ok=True)

df.to_json("data/raw/customers/customers.json", orient="records")

print("Customers extracted successfully!")