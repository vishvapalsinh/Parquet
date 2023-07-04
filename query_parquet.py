import pandas as pd

def query_and_filter_data(file_path, condition):
    df = pd.read_parquet(file_path)
    filtered_df = df.query(condition)
    return filtered_df
