import pandas as pd

file_path = r"C:\\Projects\\PVDSH_Gr15_2025\\sampled_dataset.csv"

readfile = pd.read_csv(file_path)

print("Column Data Types:")
print(readfile.dtypes, "\n")

print(f"Number of rows: {readfile.shape[0]}")
print(f"Number of columns: {readfile.shape[1]}")
