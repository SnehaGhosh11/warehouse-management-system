import pandas as pd
import glob
import os

# Set data folder path
data_folder = os.path.join(os.getcwd(), "data")

# Get all CSV and XLSX files from data folder
files = glob.glob(os.path.join(data_folder, "*.csv")) + glob.glob(os.path.join(data_folder, "*.xlsx"))

print(f"Found {len(files)} files in data folder...\n")

for file in files:
    print("\n\n===== File:", os.path.basename(file), "=====")
    try:
        # Read CSV or Excel automatically
        if file.endswith(".xlsx"):
            df = pd.read_excel(file)
        else:
            df = pd.read_csv(file)

        # Show first 5 rows and columns
        print(df.head())
        print("\nColumns:", df.columns.tolist())
    except Exception as e:
        print("Error reading", file, ":", e)
