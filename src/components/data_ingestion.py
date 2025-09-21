import pandas as pd
import os

def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

