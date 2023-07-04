from read_parquet import read_parquet_file, display_data
from write_parquet import create_dataframe, write_parquet_file
from convert_formats import convert_csv_to_parquet, convert_parquet_to_csv
from merge_parquet import merge_parquet_files
from data_analysis import perform_data_analysis
from query_parquet import query_and_filter_data

# File paths or filenames
parquet_file = 'files/sample.parquet'
csv_file = 'files/sample.csv'
output_parquet_file = 'files/output.parquet'
output_csv_file = 'files/output.csv'
file1 = 'files/file1.parquet'
file2 = 'files/file2.parquet'
merged_file = 'files/merged_file.parquet'

# Reading and displaying Parquet data
df = read_parquet_file(parquet_file)
display_data(df)

# Writing data to a Parquet file
df = create_dataframe()
write_parquet_file(df, output_parquet_file)

# Converting data between different formats
convert_csv_to_parquet(csv_file, output_parquet_file)
convert_parquet_to_csv(parquet_file, output_csv_file)

# Merging or appending Parquet files
merge_parquet_files(file1, file2, merged_file)

# Performing data analysis
mean_salary, filtered_df = perform_data_analysis(parquet_file)
print('Mean salary:', mean_salary)
print(filtered_df)

# Querying and filtering Parquet data
filtered_df = query_and_filter_data(parquet_file, 'salary > 50000')
print(filtered_df)
