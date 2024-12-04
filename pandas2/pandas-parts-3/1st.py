import pandas as pd
df1=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


s=df1['Name'][0:10]
print(s)

l=['a','b','c','d','e','f','g','h','i','j'] 
s1=pd.Series(list(s),index=l)
print(s1)
print(s[0:4])

# s2=s1.aapend(s)
# print(s2)

print(s1[4])

s4=pd.Series([1,2,3,4,5],index=[2,4,5,6,7])
s5=pd.Series([1,32,43,54,65],index=[2,9,3,8,1])
# s6=s4.append(s5)
# print(s6)

s6=s4.sub(s5)
print(s6)