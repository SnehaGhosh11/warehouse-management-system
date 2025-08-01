import pandas as pd

df = pd.read_excel("data/WMS-04-02.xlsx", header=None)  # read without assuming headers
print(df.head(20))
