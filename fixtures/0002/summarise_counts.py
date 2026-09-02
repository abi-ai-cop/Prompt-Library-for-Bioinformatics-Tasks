import pandas as pd

df = pd.read_csv("counts.csv")
counts = df.groupby("gene_id")["count"].sum()
print(counts.head())
