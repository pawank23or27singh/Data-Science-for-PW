# # use always a specific exception
# try:
#     10/0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     10/0
# except ZeroDivisionError as e:
#     print("This is my exception block",e)


# # 

import logging
logging.basicConfig(filename="error.log",level=logging.ERROR)

try:
    10/0
except ZeroDivisionError as e:
    logging.error("this is my error log{}".format(e))

# always avoid to write multiple except block

try:
    10/0
except ArithmeticError as e:
    logging.error("this is my error log{}".format(e))
except ZeroDivisionError as e:
    logging.error("this is my error log{}".format(e))
except FileNotFoundError as e:
    logging.error("this is my error log{}".format(e))

    # it is not a good habbit this form

# alaways Docoment all the error
#clear all the resorces

import logging
try :
    with open("test.txt","r") as f:
        text=f.read()
except FileNotFoundError as e:
    logging.error("this is my error log{}".format(e))
finally :
    f.close()
    # it is a right way