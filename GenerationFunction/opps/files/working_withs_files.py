f=open("test.txt",'w')
print(f.write("This is my first file to write"))
f.close()

f=open("test.txt",'a')
print(f.write("This is my second file to write"))
f.close()

data=open("test.txt",'r')
print(data.read())
data.close()

#print(data.readline())#it will read only one line

#data.seek(0) #it will start from 0th line

#print(data.readlines())  #it will read all the lines

# data.close()

data1=open("test.txt",'r')
for i in data1:
    print(i)


#find the size
# import os

# print(os.path.getsize("test.txt"))

#delete
#print(os.remove('test.txt'))

#
f=open("test.txt",'w')
print(f.write("This is my first file to write and its is my fovorite file"))
f.close()

#rename
import os
os.rename('test1.txt','new.txt')

#new capy
import shutil

shutil.copy('test.txt','copy.txt') 

with open('test.txt') as f:
    print(f.read())
