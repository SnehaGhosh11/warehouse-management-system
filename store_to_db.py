import pandas as pd
from sqlalchemy import create_engine

# Load mapped data
df = pd.read_csv("output_mapped_sales.csv")

# Create SQLite DB
engine = create_engine("sqlite:///wms.db", echo=False)

# Store to database
df.to_sql("sales", con=engine, if_exists="replace", index=False)
print("Data stored in wms.db (sales table)")

# Quick test: Read back from DB
read_df = pd.read_sql("SELECT * FROM sales LIMIT 5", con=engine)
print(read_df)
