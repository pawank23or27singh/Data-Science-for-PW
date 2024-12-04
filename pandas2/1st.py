# import pandas as pd

# pd.read_csv("customers.csv")
# # df = pd.read_csv("customers.csv")
# # print(df.head())
# # df.tail()
# pd.open("customers.csv")

# print(pd.columns)
# pf=pd.read_csv("customers.csv")
# print(pf)
# 
import pandas as pd
from pandas import DataFrame
# file_path =("path/to/customers.csv")  # Replace with the actual file path
# df = pd.read_csv(file_path)
# df.head()
file_path = 'C:/Users/pawan/Desktop/python/Pwds/Pandas/pandassss/customers.csv'
df1= pd.read_csv(file_path)
print(df1.head())
print(df1.tail())
print(df1.tail(3))
# print(list(df1.columns))
# print(df1[['first_name', 'last_name']])
# print(df1[['last_name', 'first_name']])
# print(df1[['last_name', 'first_name']].head(3))
# print(df1[['last_name', 'first_name']].tail(3))
# print(df1.dtypes)
# print(df1.describe())
# print(df1.info())
# print(df1.head(3))
# print(df1.tail(3))
# print(df1['last_name'])
# print(df1.info())

# df.dtypes()
# df.describe()
# df.info()
# df.head(3)
# df.tail(3)
# df['last_name']
# df['last_name'].head(3)
# df['last_name'].tail(3)
# df['last_name'].describe()
# df['last_name'].info()
