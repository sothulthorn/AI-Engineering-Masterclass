"""
Pandas Data Structures
- Series
- DataFrame
"""
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

# Loading Data
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')

# Saving Data
df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)

# Basic DataFrame Operations
# Viewing Data
print(df.head())
print(df.tail(3))
print(df.info())
print(df.describe())

# Selecting and Indexing
# Selecting columns
print(df["Name"])
# Filtering rows
print(df[["Name", "Age"]])
print(df[df["Age"] > 25])
# Selecting by position
print(df.iloc[0])
print(df.iloc[:, 0])
# Selecting by label
print(df.loc[0])
print(df.loc[:, "Name"])