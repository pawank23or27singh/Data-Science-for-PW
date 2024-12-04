# numpy arry manipulation
import numpy as np
# arr=np.random.randint(1,10,(3,4))
# print(arr)
# arr1=arr.reshape(2,6)
# print(arr1)

# arr2=arr.reshape(2,-23456)
# print(arr2)


# arr3=arr.flatten()
# print(arr3)


# arr4=np.array([1,2,3,4,5,6,7])
# arr5=arr4.ndim
# print(arr5)

# arr5=np.expand_dims(arr4,axis=1)
# print(arr5)
# arr6=np.expand_dims(arr4,axis=0)
# print(arr6)

# data=np.array([[1],[2],[3]])
# print(data)

# data1=np.squeeze(data)
# print(data1)

# arr6=np.repeat(arr4,3)
# print(arr6)


# arr7=np.roll(arr4,2)
# print(arr7)
# print(arr4)

# arr8=np.diag(arr4)
# print(arr8)

# # Binary operation
# arr9=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr10=np.array([[2,3,4,5,6],[7,8,9,10,11]])
# arr11=arr9+arr10
# arr12=arr9-arr10
# arr13=arr9*arr10
# arr14=arr9/arr10
# arr15=arr9**arr10
# arr16=arr9%arr10
# print(arr11)
# print(arr12)
# print(arr13)
# print(arr14)
# print(arr15)
# print(arr16)


# arr17=arr9&arr10
# arr18=arr9|arr10
# arr19=arr9^arr10
# arr20=~arr9
# print(arr20)
# print(arr17)
# print(arr18)
# print(arr19)

# arr21=arr9>arr10
# arr22=arr9<arr10
# arr23=arr9>=arr10
# arr24=arr9<=arr10
# arr25=arr9==arr10
# arr26=arr9!=arr10
# print(arr21)
# print(arr22)
# print(arr23)
# print(arr24)
# print(arr25)
# print(arr26)


# Numpy string function

arr27=np.char.add(['hello'],['world'])
print(arr27)
arr28=np.char.upper(arr27)
print(arr28)

arr29=np.char.title(arr27)
print(arr29)

arr30=np.char.capitalize(arr27)
print(arr30)


# numpy mathematical function
arr31=np.array([[1,2,3,4,5],[6,7,8,9,10],[3,4,6,7,8]])
arr32=np.array([[1,2,3,4,5],[6,7,8,9,10],[3,4,6,7,8]])
arr33=np.sin(arr31)
arr34=np.cos(arr32)
print(arr33)
print(arr34)
arr35=np.power(arr31,2)
print(arr35)
arr35=np.std(arr31)
arr36=np.var(arr32)
arr37=np.mean(arr31)
arr38=np.median(arr32)
arr39=np.max(arr31)
arr40=np.min(arr32)
arr41=np.sum(arr31)
print(arr41)
print(arr40)
print(arr39)
print(arr38)
print(arr37)
print(arr36)
print(arr35)


