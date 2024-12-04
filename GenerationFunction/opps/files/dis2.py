data={
    "name":"pawan",
    "age":23,
    "city":"patna",
    "country":"India",
    "phone":"1234567890",
    "subject" : ["data science","web dev","big data","data analytics"]
}
import json
with open("data.json","w") as f:#write
    json.dump(data,f)
print(data)
with open("data.json","r") as f:#read 
    data1=json.load(f)
print(data1)


#1,2,3,4,4
# 1,2,3,4,5
#comma seperated values
import csv
data=[["name","age","city","country","phone","subject"],
      ["pawan",23,"patna","India","1234567890","data science"]]
with open("data.csv","w") as f:
    writer=csv.writer(f)
    for i in data:
        print(writer.writerow(i))
    ##print(data)



#reader  csvdata
import csv
with open("data.csv","r") as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)

# binary data 
#koi bhi picture or video ke andar binary data hai 0 or 1 ke form me wahi  hota hai binary data
with open("test.bin","wb") as f:
    f.write(b"\x01\x02\x03\x04\x05")
    print(f)

    #read binary data
with open("test.bin","rb") as f:
    data=f.read()
    print(data)