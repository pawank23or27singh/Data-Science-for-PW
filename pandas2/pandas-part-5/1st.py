# import pandas as pd
# data={'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]}
# df=pd.DataFrame(data)
# # print(df)

# df.set_index('a',inplace=True)#a ko index bana diya tab ye karenge
# print(df)

# # reset index
# df=df.reset_index()
# print(df)


# # 
# data={'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]}
# df1=pd.DataFrame(data,index=['a','b','c','d','e'])
# # print(df1)

# # # reidexing
# # df2=df1.reindex(['b','c','d','a','e'])
# # print(df2)

# # # iteration row wise

# # for i,j in df1.iterrows():
# #     print( i,j)

# # iterrate item
# # for i in df1.iteritems():
# #     print(i)

# data2=list(df['a'])
# print(data2)

# data3=[i for i in df['a']]
# print(data3)

# # canctination perform
# def test(x):
#     return x.sum()
# data4=df1.apply(test)
# print(data4)

# # maltiplication 
# df3=df1[['a','b']]
# print(df3)
# df4=df3.applymap(lambda x : x**2)
# print(df4)

# # sorting by index
# df5=df1.sort_index()
# print(df5)

# # sorting by value
# df6=df1.sort_values(by='a')
# print(df6)
# # ascending false
# df7=df1.sort_values(by='a',ascending=False)
# print(df7)

# # dataframe show the different options of display size of words
# pd.set_option('display.max_colwidth',1000)
# df8=pd.DataFrame({"Description":["Applying machine learning with real-world datasets teaches valuable skills like cleaning data and handling class imbalance. This guide provides five weekend projects with suggested datasets, goals, and focus areas, such as predicting house prices, sentiment analysis of tweets customer segmentation churn prediction and movie"]})
# print(df8)
# # length
# df9=df8['len']=df8['Description'].apply(len)
# print(df9)


# # word count
# t="i am a good boy"
# print(t.split())

# df10=df8['word_count']=df8['Description'].apply(lambda x : len(x.split()))
# print(df10)

# # statistical function
# print(df1)
# df11=df1['a']
# df12=df11.mean()
# print(df12)

# df13=df11.sum()
# print(13)
# df14=df11.count()
# print(df13)
# df15=df11.max()
# print(df15)
# df16=df11.min()
# print(df16)
# df17=df11.median()
# print(df17)
# df18=df11.std()
# print(df18)
# df19=df11.var()
# print(df19)

# data4=pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9,10]})
# print(data4)

# df20=data4['a'].rolling(window=3)
# df21=df20.mean()# window size is 3 means 3 values will be considered and ese ham change bhi kar sakte hai
# print(df21)

# df22=df20.max()
# print(df22)

# df23=df20.min()
# print(df23)

# df24=df20.std()
# print(df24)

# df25=df20.var()
# print(df25)

# # cammulative sum
# df26=data4['a'].cumsum()
# print(df26)

# # Date functionality
# date=pd.date_range(start= "2023-01-01",end="2023-02-10")

# print(date)


# date_df=pd.DataFrame({'date':date})
# print(date_df)

# data_df2=pd.DataFrame({"date":['2023-01-01','2023-01-02','2023-01-10']})
# print(data_df2)

# data2=data_df2.dtypes
# print(data2)

# data3=data_df2['year']=data_df2['updated'].dt.day
# print(data_df2)

# data visualization library
import pandas as pd
import matplotlib.pyplot as plt
# d=pd.Series([1,2,3,4,5,6,7,8,9,10])

# data5 = d.plot()
# print(data5)
# plt.show()
df=pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9,10],'b':[1,2,3,4,5,9,7,3,10,6]})

# data6=df.plot()
# print(data6)

df1=df.plot.pie()
print(df)
plt.show()
