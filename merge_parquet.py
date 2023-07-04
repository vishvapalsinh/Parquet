import pandas as pd

def merge_parquet_files(file1, file2, merged_file):
    df1 = pd.read_parquet(file1)
    df2 = pd.read_parquet(file2)
    merged_df = pd.concat([df1, df2], ignore_index=True)
    merged_df.to_parquet(merged_file)
