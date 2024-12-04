import matplotlib.pyplot as plt
import numpy as np


# y=np.linspace(0,10,100)
# plt.plot(y)
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# # plt.show()

# # plt.plot(x,y)
# plt.title("this is my title")
# plt.xlabel("this is x")
# plt.ylabel("this is y")
# plt.show()


# x=np.random.rand(50)
# y=np.random.rand(50)

# colours=np.random.rand(50)
# sizes=np.random.rand(50)*100
# print(plt.scatter(x,y, c=colours))
# print(plt.scatter(x,y, s=sizes))
# plt.show()


# print(plt.scatter(x,y, c=colours))
# plt.show()


# print(plt.scatter(x,y))
# plt.show()

# plt.plot(x,y)
# colours=np.random.rand(50)
# sizes=np.random.rand(50)*100

# print(plt.scatter(x,y, c=colours))
# print(plt.scatter(x,y, s=sizes, c=colours,alpha=0))
# plt.xlable("x axis")
# plt.y.lable("y axis")

# plt.show()

# catoricalVs nomerical

# x=['a','b','c','d' ,'e','f']
# y=np.random.rand(6)
# print(y)
# plt.bar(x,y)
# # plt.xlable("x axis")
# # plt.ylable("y axis")
# plt.show()


# #  horizontal bar graph

# plt.barh(x,y)
# # plt.xlable("x axis")
# # plt.ylable("y axis")
# plt.show()

# x = np.linspace(0, 20, 100)
# y=np.linspace(0,10,100)  
# # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.title("this is my title")
# plt.xlabel("this is x")
# plt.ylabel("this is y")
# plt.show()


# plt.plot(x,y)
# plt.figure(figsize=(6,3))
# plt.show()

# plt.title("this is my title")
# plt.xlabel("this is x")
# plt.ylabel("this is y")
# plt.show()


# x=np.random.rand(50)
# y=np.random.rand(50)

# colours=np.random.rand(50)
# sizes=np.random.rand(50)*100
# plt.scatter(x,y, c='b',s=sizes,alpha=1,marker='v') # c= any colours you take it 
# plt.show()


# data=[1,3,4,5,6,7,7,8,9,1,2,3,3,5,]
# plt.hist(data)
# plt.show()

x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()
