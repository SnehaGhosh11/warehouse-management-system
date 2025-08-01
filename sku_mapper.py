import pandas as pd

class SkuMapper:
    def __init__(self, mapping_file):
        # Handle Excel with unusual headers
        if mapping_file.endswith(".xlsx"):
            df = pd.read_excel(mapping_file, header=2)  # read from row 3
        else:
            df = pd.read_csv(mapping_file)

        # Normalize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # If columns are misaligned (like unnamed), handle manually
        if 'sku' not in df.columns or 'msku' not in df.columns:
            # Find column index based on known position
            df = df.iloc[:, [7, 8]]  # columns at index 7 and 8
            df.columns = ["sku", "msku"]

        self.mapping_df = df.dropna(subset=["sku", "msku"])

    def map_skus(self, sales_file):
        # Load sales data
        if sales_file.endswith(".xlsx"):
            sales_df = pd.read_excel(sales_file)
        else:
            sales_df = pd.read_csv(sales_file)

        # Normalize column names
        sales_df.columns = [c.strip().lower() for c in sales_df.columns]

        # If "SKU" exists but name is lowercase
        if 'sku' not in sales_df.columns:
            raise Exception("Sales file must have SKU column")

        # Merge mapping
        merged = sales_df.merge(self.mapping_df, on="sku", how="left")

        # Warn if some SKUs not mapped
        missing = merged[merged['msku'].isna()]
        if not missing.empty:
            print("Warning: Missing mappings for SKUs:", missing['sku'].unique())

        # Save output
        merged.to_csv("output_mapped_sales.csv", index=False)
        print("Mapping complete! Output saved to output_mapped_sales.csv")

        return merged
