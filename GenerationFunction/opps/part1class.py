class skills1:
    def __init__(self,phone_number,email_id,student_id):# __init__ function  data ko pass karne ke liye banaya jata hai(initialization) is a constructor in python class we use __init__
        self.phone_number1=phone_number
        self.email_id1=email_id
        self.student_id1=student_id
    def return_student_details(self):
        return self.phone_number1,self.email_id1,self.student_id1
pawan=skills1(1234567890,"pawan@123",123)
##self is a keyword which is used to represent the instance of the class in python
print(pawan.return_student_details()) 