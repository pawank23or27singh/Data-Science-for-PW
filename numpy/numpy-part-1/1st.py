import numpy as np
# list=[1,2,34]
# ar=np.array(list)
# print(ar)
# p=type(ar)
# print(p)

# df1=np.array([[1,2],[3,4]])
# print(df1)

# same same
# df2=np.asanyarray(df1)
# print(df2)

# # matrix 
# b=np.matrix(df1)
# print(b)

# deep cappy
# c=np.asarray(list)
# print(c)
# print(p)
# c=p
# print(c)
# c[1]=100
# print(c)
# d=np.asanyarray(df1)
# print(d)
# print(c)
# c[1]=400
# print(c)

# e=np.fromfunction(lambda i,j: i==j,(3,3))
# print(e)

# f=np.fromfunction(lambda i,j: i*j,(3,3))
# print(f)

# for i in np.nditer(f):
#     print(i)


# iterable=(i*i for i in range(5))
# print(iterable)

# for i in iterable,float:
#     print(i)

# g=np.fromstring('1 2',dtype=int,sep=' ')
# print(g)

# ar22=np.array([[1,2],[3,4]])
# print(ar22)
# p=list(range(3))
# print(p)


# ar4=np.zeros((3,3,4))
# print(ar4)

# ar5=np.ones((3,4))
# print(ar5)
# print(ar5*6)


# ar6=np.empty((3,6))
# print(ar6)

# arr=np.random.random((3,3))
# print(arr)

import pandas as pd
# p=pd.DataFrame(arr)
# print(p)

# arr2=np.random.rand(3,3)
# print(arr2)

# arr3=np.random.randint(3,3,(5,4))
# print(arr3)


# arr4=pd.DataFrame(np.random.random(3,3,(5,4))).to_csv('test_csv')
# print(arr4)

# arr=np.random.random((3,3))
# arr7=arr.reshape(3,3)
# print(arr7)

# arr7=arr[1][1]
# print(arr7)

# matrix multiplication
# arr8=np.array([[1,2],[3,4]])
# arr9=np.array([[1,2],[3,4]])
# arr10=np.dot(arr8,arr9)
# print(arr10)

# arr10=np.array([[1,2],[3,4]])
# arr11=np.array([[1,2],[3,4]])
# print(arr10@arr11)


# numpy broadcasting
arr12=np.array([[1,2],[3,4]])
arr13=np.array([1,2])
print(arr12+arr13)