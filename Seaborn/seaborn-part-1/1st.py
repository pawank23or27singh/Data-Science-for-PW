import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")

iris=sns.load_dataset('iris')
# print(iris)
 
# ar1=sns.scatterplot(x=iris.sepal_length,y=iris.sepal_width)
# print(ar1)
# plt.show()

# ar2=sns.scatterplot(x=iris.sepal_length,y=iris.petal_length)
# print(ar2)
# plt.show()

# ar1=sns.scatterplot(x=iris.sepal_length,y=iris.petal_width)
# print(ar1)
# plt.show()


# sns.displot(iris['sepal_length'])
# plt.show()


df1=sns.load_dataset("tips")
# print(df1)

# df2=sns.scatterplot(x=tips.total_bill,y=tips.tip)
# print(df2)
# plt.show()

# df3=tips['smoker'].value_counts().plot(kind='bar')
# print(df3)
# plt.show()

# sns.relplot(x="total_bill", y="tip", data=tips,hue="smoker")
# plt.show()

# df4=tips.head()
# print(df4)

# sns.relplot(x="total_bill", y="tip", data=tips,hue="size")
# plt.show()

# df5=tips['size'].value_counts()
# print(df5)


# sns.relplot(x="total_bill", y="tip", data=tips,style="size")
# plt.show()


# sns.relplot(x="total_bill", y="tip", data=tips,style='size',hue="time")
# plt.show()

# sns.catplot(x="day", y="total_bill", data=tips)
# plt.show()

# sns.catplot(x='smoker',y='tip',data=tips)
# plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()

sns.pairplot(tips)
plt.show()


sns.jointplot(iris)
plt.show()

sns.pairplot(iris)
plt.show()