import pandas as pd
df1=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# df2=df1.columns
# print(df2)

# print(df1.head())

# # passengerd id gayb karna hai to 

# df3=df1.drop('PassengerId',axis=1)
# print(df3)

# df3=df1.drop('PassengerId',axis=1,inplace=True)
# print(df3)

# print(df1)

# df4=df1.drop([0,1,2])
# print(df4)


# parmanently drop
# df4=df1.drop([0,1,2],inplace=True)
# print(df4)

# parmanently drop ke bad set of columns

# df1.set_index("Name")
# print(df1)

# # reset index is used to reset the index
# df1.reset_index("Name")
# print(df1)

# ak data fram banate hai jo disnery format hai usko convert karna dataframe me
# d={'key1':[1,2,3,4,5],'key2':['a','b','c','d','e'],'key3':[4,5,6,7,8]}
# print(pd.DataFrame(d))


# #   taxonomy
# file_path="Users\pawan\Desktop\python\Pwds\pandassss\pandas-part-4\taxonomy.csv"
# df2=pd.open(file_path)
# df2=pd.read_csv(file_path)
# print(df2)

# print(df2.columns)

#  

# group Fare by survived or not

# df3=df1.groupby('Survived')
# print(df3)

# print(df3.sum())

#  avg of fare
# df4=df1.groupby('Survived').mean() 
# print(df4)

# g=df1.groupby('Survived')['Fare'].mean()
# print(g)

# g1=df1.groupby('Pclass')

# print(g1.sum())
# print(g1.mean())

# g1=df1.groupby('Pclass')['Fare'].mean()
# print(g1)
# print(g1.max().transpose())

# data frame
# df7=df1[['PassengerId','Survived','Pclass']][0:5]
# df8=df1[['PassengerId','Survived','Pclass']][0:10]

# print(df7)
# print(df8)

# # cancatination
# df9=pd.concat([df7,df8])

# print(df9)


# # cancatination adding axis
# df10=pd.concat([df7,df8],axis=1)
# print(df10)
# # nan ke jagah fill Pawan
# print(df10.fillna('Pawan'))


# data1=pd.DataFrame({'key1':[1,2,3,4,5],'key2':[76,67,8,97,32],'key3':[24,45,56,17,48]},index=[0,1,2,3,4])
# # print(data1)

# data2=pd.DataFrame({'key4':[54,43,4,5,6],'key5':[9,7,6,74,32],'key6':[65,67,33,45,23]})
# # print(data2)

# # # marge operation in inner operation
# # data3=pd.merge(data1,data2,how='right',how='inner',how='outer',how='left',on='key1')
# # print(data3)

# # join

# data4=data1.join(data2)
# print(data4)
# # inner

# data5=data1.join(data2,how='inner')
# print(data5)

# # outer

# data6=data1.join(data2,how='outer')
# print(data6)

# # cross

# data7=data1.join(data2,how='cross')
# print(data7)

# print(df1)

# apply function on the dataframe
# df1['Fare_INR']=df1['Fare'].apply(lambda x: x*80)

# print(df1.head())

# outer function
def euro_inr(x):
    return x*80
df1['Fare_INR']=df1['Fare'].apply(euro_inr)
print(df1.head())

# name columns
df1['Name_length']=df1['Name'].apply(len)
print(df1.head())

# cat_fare
def cat_fare(x):
    if x<10:
        return 'cheap'
    elif x>=10 and x<20:
        return 'mid'
    else:
        return 'exp'

df1['Fare_cat']=df1['Fare'].apply(cat_fare)
print(df1.head())