# data base

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Pawan@123",
    database="pwskills"
)
mycursor=mydb.cursor()
mycursor.execute("select * from student")
result=mycursor.fetchall()
for i in result:
    print(i)