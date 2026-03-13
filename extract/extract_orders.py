import requests
import pandas as pd
import os

url = "https://fakestoreapi.com/carts"

response = requests.get(url)

print("Status Code:", response.status_code)

# check if request worked
if response.status_code != 200:
    print("API request failed")
    print(response.text)
    exit()

data = response.json()

df = pd.DataFrame(data)

os.makedirs("data/raw/orders", exist_ok=True)

df.to_json("data/raw/orders/orders.json", orient="records")

print("Orders extracted successfully!")