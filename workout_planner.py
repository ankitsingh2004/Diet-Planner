import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR,"workout_data.csv")

def workout_plan(level, location):
    df = pd.read_csv(DATA_PATH)

    if location == "home":
        return df[df["level"] == level].head(5)
    else:
        return df.sample(6)

