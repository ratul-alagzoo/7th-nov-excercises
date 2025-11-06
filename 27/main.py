import seaborn as sns
import polars as pl

df = sns.load_dataset("iris")
pl_df = pl.from_pandas(df)
print(pl_df.describe())

min_idx = pl_df.select(pl.col("petal_length").arg_min()).item()
max_idx = pl_df.select(pl.col("petal_length").arg_max()).item()
print("Index of smallest petal length:", min_idx)
print("Index of largest petal length:", max_idx)