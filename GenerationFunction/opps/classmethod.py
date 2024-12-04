class pwskill1:
    def __init_(self,phone_number,email_id,student_id):
        self.phone_number=phone_number
        self.email_id=email_id
        self.student_id=student_id

    @classmethod
    def details(cls,phone_number,email_id,student_id):
        return cls(phone_number,email_id,student_id)

    def return_student_details(self):
        print(self.phone_number,self.email_id,self.student_id)

pawan=pwskill1.details(1234567890,"pawan@123",123)
print(pawan.return_student_details())