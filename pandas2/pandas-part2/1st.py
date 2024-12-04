import pandas as pd
df1=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#print(df1)
#print(df1.head())
# print(type(df1))
# print(df1.dtypes)
# print(df1.describe())
# print(df1.dtypes)
# df2=df1[['Name', 'Age','Sex','Ticket',]]
# print(df2)
# df1.dtypes=='object'
# print(df1.dtypes[df1.dtypes=='object'])
# print(df1.dtypes[df1.dtypes=='object'].index)
# print(df1[df1.dtypes[df1.dtypes=='object'].index].describe())


# print(df1.dtypes=='float64')
# print(df1.dtypes[df1.dtypes=='float64'])
# print(df1.dtypes[df1.dtypes=='float64'].index)
# print(df1[df1.dtypes[df1.dtypes=='float64'].index].describe())


# print(df1.columns)
# print(df1[['Ticket','Cabin']][4:11:2])


# df3=df1['new_columns']=0
# print(df1.head(3),df3)
# df4=df1['new_columns']=df1['PassengerId']+df1['Age']
# print(df4.head(3))


# print(df1.head())


# print(pd.Categorical(df1['Pclass']))

# print(pd.Categorical(df1['Age']))


# print(df1['Cabin'].unique())

# print(df1['Age']>50)

# df5=df1[df1['Age']>50]
# print(df5)


# print(df1['Fare']>32.204208)
# # print(df1['Fare'].max())
# print(df1[df1['Fare']>32.204208])


# print(df1['Fare']==0)

# print(df1[df1['Sex']=='male'])

# print(df1[df1['Sex']=='female'])

# print(df1['Pclass']==1)
# print(df1[df1['Pclass']==1])


# print(df1['Survived']==1)
# print(df1[df1['Survived']==1])

# df6=df1['Sex']=='female'
# print(df6)

# print(df1[(df1['Sex']=='female') & (df1['Fare']>32.204208)])
# print(df1[(df1['Sex']=='female') | (df1['Fare']>32.204208)]) #koi ak bhi condition hai true h then print  


# print(max(df1['Fare']))

# print(df1[df1['Fare']==max(df1['Fare'])])
# print(df1[df1['Fare']==max(df1['Fare'])]['Name'])


# print(df1.head())
# print(df1[0:2])#row
# print(df1[0::2])#columns

print(df1[['PassengerId','Survived','Pclass']])
print(df1[['PassengerId','Survived','Pclass']][0:2])
print(df1.iloc[0:2])


print(df1[['PassengerId','Survived','Pclass']])
print(df1.loc[0:2,['PassengerId','Survived','Pclass']]) 