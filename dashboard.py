import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Connect DB
engine = create_engine("sqlite:///wms.db", echo=False)

# Load sales table
df = pd.read_sql("SELECT * FROM sales", con=engine)

st.title("Warehouse Management Dashboard")

# Summary Metrics
total_items = df['quantity'].sum()
unique_skus = df['sku'].nunique()
mapped_skus = df['msku'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Quantity", total_items)
col2.metric("Unique SKUs", unique_skus)
col3.metric("Mapped MSKUs", mapped_skus)

# Chart 1: Quantity by MSKU
if 'msku' in df.columns:
    fig = px.bar(df.groupby('msku')['quantity'].sum().reset_index(),
                 x='msku', y='quantity', title='Quantity by MSKU')
    st.plotly_chart(fig)

# Chart 2: Top Products
fig2 = px.bar(df.groupby('product name')['quantity'].sum().sort_values(ascending=False).head(10).reset_index(),
              x='product name', y='quantity', title='Top 10 Products')
st.plotly_chart(fig2)
