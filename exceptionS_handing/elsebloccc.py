# import io
# try:
#     f=open("test1.txt","r")
#     f.write(" write something")
#     f.close()
# except Exception as e:
#     print("This is my exception block",e)
# else:
#     print("this will be executed only if there is no exception")
#     f.close()


# import io
# try:
#     f=open("test.txt","w")
#     f.write(" write something")
#     f.close()
# except Exception as e:
#     print("This is my exception block",e)
# else:
#     print("this will be executed only if there is no exception")
#     f.close()


# finally block  will always execute
import io
try:
    f=open("test3.txt","w") 
    f.write(" write something")
    f.close()
finally:
    print("finally block will always execute")