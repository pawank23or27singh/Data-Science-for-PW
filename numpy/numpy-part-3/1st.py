# sort search & counting function
import numpy as np
# arr=np.array([[76,78,89,61,2,3],])
# arr1=np.sort(arr)
# print(arr1)


# arr3=np.array([[76,78,89,61,2,3],])
# arr2=np.searchsorted(arr3,84)
# print(arr2)

arr4=np.array([76,78,89,61,2,3])
arr5=np.count_nonzero(arr4)
print(arr5)

arr6=np.array([76,78,89,61,2,3])
arr7=np.nonzero(arr6)
print(arr7)

arr8=np.array([76,78,89,61,2,3])
arr9=np.where(arr8%2==0)
print(arr9)


# byte swapping
arr10=np.array([76,78,89,61,2,3])
arr11=arr10.byteswap()
print(arr11)

# copies & views
arr12=np.array([76,78,89,61,2,3])

arr13=arr12.view()# shallow copy
print(arr13)

arr14=arr12.copy() #deep copy
print(arr14)


# Matrix Library

import numpy.matlib as nm

arr15=nm.zeros((3,3))
print(arr15)

arr16=nm.ones((3,4))
print(arr16)

arr17=nm.eye(5)
print(arr17)


# numpy -linear algebra

arr18=np.array([[1,2],[3,4]])
arr19=np.random.randint([[1,2],[3,4]])
arr20=np.random.randint([[13,2],[3,14]])
arr19=np.linalg.det(arr18)

arr21=np.dot(arr19,arr20)
print(arr21)

arr22=arr19@arr20
print(arr22)