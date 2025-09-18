# Grouping Data by Categories
grouped = df.groupby('common_column')

for name, group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()

# Aggregation Function
# groupby
df.groupby('category_column')["numeric_column"].mean()
df.groupby('category_column').agg({"numeric_column":["mean", "max", "min"]})

# pivot_table
pivot = df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean",
)

# custom aggregation
def range_func(x):
    return x.max() - x.min()

df.groupby('category_column').agg({"numeric_column":range_func})

# Calculating Summary Statistics for Grouped Data
df.groupby('category_column')["numeric_column"].mean()
df.groupby('category_column')["numeric_column"].max()
df.groupby('category_column')["numeric_column"].min()

# Multi-Aggregation
df.groupby('category_column').agg({"numeric_column":["mean", "max", "min"]})