import pandas as pd

def create_dataframe():
    data = {'Name': ['John', 'Jane', 'Alice'],
            'salary': [25000, 30000, 350000]}
    df = pd.DataFrame(data)
    return df

def write_parquet_file(df, file_path):
    df.to_parquet(file_path)
