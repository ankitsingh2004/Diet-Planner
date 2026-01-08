import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "food_data.csv")

def diet_plan(food_type, budget):
    df = pd.read_csv(DATA_PATH)

    filtered = df[
        (df["type"] == food_type) &
        (df["budget"] == budget)
    ]

    return filtered.sample(min(4, len(filtered)))
