import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["date_posted"])
    return df
