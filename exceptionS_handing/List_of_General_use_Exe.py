# import io
# try:
#     int ("Pawan")
# except (ValueError,TypeError) as e:
#     print(e)

#     # kyuki string value ko ham int me likh rahe hai jo ki galat hai


# import io 
# try :
#     int ("pawan")
# except:
#     print("This is my exception block")


# import io
# try:
#     import Pwds
# except ImportError as e:
#     print(e)
# 10/4

# import io
# try:
#     10/0
# except ZeroDivisionError as e:
#     print(e)


# import io
# try:
#     d={"key":"value",1:[1,2,3,4],"key2":"value2"}
#     print(d["key3"])
# except KeyError as e:
#     print(e)

import io
try:
    10/0
except ArithmeticError as e:
    print(e)

try:
    123+"pawan"
except TypeError as e:
    print(e)

try:
    with open("test.txt","r") as f:
        text=f.read()
except FileNotFoundError as e:
    print(e)


# there are many type of error

try:
    with open("test.txt","r") as f:
        text=f.read()
except Exception as e:
    print(e)
except FileNotFoundError as e:
    print("text",e)


# 
def test(file):
    try:
        with open(file,"r") as f:
            text=f.read()
    except FileNotFoundError as e:
        raise e

