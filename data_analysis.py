import pandas as pd

def perform_data_analysis(file_path):
    df = pd.read_parquet(file_path)
    mean_salary = df['salary'].mean()
    filtered_df = df[df['salary'] > 50000]
    return mean_salary, filtered_df

