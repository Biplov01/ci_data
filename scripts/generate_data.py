import pandas as pd
import numpy as np
import os

np.random.seed(42)

os.makedirs("data/raw", exist_ok=True)

products = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple"]

data = {
    "product": np.random.choice(products, 20),
    "quantity": np.random.randint(1, 20, 20),
    "price": np.random.randint(1, 10, 20)
}

df = pd.DataFrame(data)

# Introduce missing values
df.loc[3, "quantity"] = None
df.loc[7, "price"] = None

df.to_csv("data/raw/sample.csv", index=False)

print("Synthetic data created in data/raw/sample.csv")
