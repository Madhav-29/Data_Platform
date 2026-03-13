import requests
import pandas as pd
import os

url = "https://fakestoreapi.com/products"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

os.makedirs("data/raw/products", exist_ok=True)

df.to_json("data/raw/products/products.json", orient="records")

print("Products extracted successfully!")