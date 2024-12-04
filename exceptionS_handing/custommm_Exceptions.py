# import io
# age=int (input("Enter your age:"))
# if age<0:
#     print("Age cannot be negative")
# elif age>150:
#     print("Age cannot be greater than 150")
# else:
#     print("Age is valid")


import io
class valid_age(Exception):
    def __init__(self,msg):
        self.msg=msg

def validate_age(age):
    if age<0:
        raise valid_age("Age cannot be negative")
    elif age>150:
        raise valid_age("Age cannot be greater than 150")
    else:
        print("Age is valid")

try:
    age=int(input("Enter your age:"))
    validate_age(age)
except valid_age as e:
    print(e)


