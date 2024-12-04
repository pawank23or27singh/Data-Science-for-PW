# l=[1,2,3,4,34,[2,3,4,],"pawan","kumar"]
# l1_int=[]
# l2_str=[]
# for i in l:
#     if type(i)==list:
#         for j in i:
#             if type(j)==int:
#                 l1_int.append(j)
#     elif type(i)==int :
#         l1_int.append(i)
#     else:
#         if type(i)==str:
#             l2_str.append(i)
# print(l1_int)
# print(l2_str)




#logging is used to print in the file
import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
l=[1,2,3,4,34,[2,3,4,],"pawan","kumar"]
l1_int=[]
l2_str=[]
for i in l:
    logging.info("We are iterating through our list and our local variable is i ")

    if type(i)==list:
        logging.info("We are iterating through our list and our local variable is i and its type is list")
        for j in i:
            logging.info("We are iterating through our list and our local variable is j and its type is list")
            if type(j)==int:
                logging.info("We are iterating through our list and our local variable is j and its type is int") 
                l1_int.append(j)
    elif type(i)==int :
        l1_int.append(i)
    else:
        if type(i)==str:
            l2_str.append(i)
# print(l1_int)
# print(l2_str)
import logging

# Configure logging
logging.basicConfig(filename="test.log", level=logging.INFO)

l = [1, 2, 3, 4, 34, [2, 3, 4], "pawan", "kumar"]
l1_int = []
l2_str = []

# Iterate over the elements in list `l`
for i in l:
    logging.info(f"Iterating through the list; current element: {i}")

    if type(i) == list:
        logging.info(f"Current element is a list: {i}")
        for j in i:
            logging.info(f"Iterating through sublist; current sub-element: {j}")
            if type(j) == int:
                logging.info(f"Sub-element is an integer: {j}")
                l1_int.append(j)
    elif type(i) == int:
        logging.info(f"Current element is an integer: {i}")
        l1_int.append(i)
    elif type(i) == str:
        logging.info(f"Current element is a string: {i}")
        l2_str.append(i)




