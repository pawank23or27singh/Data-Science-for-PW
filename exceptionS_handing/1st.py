import io
try:
    f=open("test.txt","w")
    f.write(" write something")
    f.close()
except Exception as e:
    print("This is my exception block",e)
