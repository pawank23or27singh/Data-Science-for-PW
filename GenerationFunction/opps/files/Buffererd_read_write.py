import io
with open("test.txt","wb") as f:
    file=io.BufferedWriter(f)
    file.write(b"This is my first file to write")
    file.write(b"\nThis is my second file to write")
    file.flush()
print(file)

#read 
with open("test.txt","rb") as f:
    file=io.BufferedReader(f)
    data = file.read()# yaha la size de skte hai ki kaha tak print karna hai(12)
    print(file.read())