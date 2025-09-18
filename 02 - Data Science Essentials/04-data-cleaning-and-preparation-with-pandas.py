# Drop Missing Values
import pandas as pd

df = df.dropna()    # drop row
df = df.dropna(axis=1) # drop column

# Fill Missing Values
df["column_name"] = df["column_name"].fillna(0)
df.fillna(method="ffill")
df.fillna(method="bfill")

# Interpolation
df["column_name"] = df["column_name"].interpolate()

# Data Transformation
# Renaming Columns
df = df.rename(columns={"column_name": "new_column_name"})

# Changing Data Types
df["column_name"] = df["column_name"].astype(float)
df["column_name"] = pd.to_datetime(df["column_name"])

# Modifying the column
df["new_column"] = df["existing_column"] * 2

# Combining and Merging DataFrames
# Concatenation
combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

# Merging
merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")

# Joining
joined = df1.join(df2, how="left", on="common_column")
