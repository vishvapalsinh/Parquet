import pandas as pd

def convert_csv_to_parquet(csv_file, parquet_file):
    df = pd.read_csv(csv_file)
    df.to_parquet(parquet_file)

def convert_parquet_to_csv(parquet_file, csv_file):
    df = pd.read_parquet(parquet_file)
    df.to_csv(csv_file, index=False)
