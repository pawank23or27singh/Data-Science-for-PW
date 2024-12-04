class pwskills:
    def student_details(self,name,age,gender):
        print(name,age,gender)

pw=pwskills()
pw.student_details("pawan",23,"male")
# print(pw.student_details)

class pwskills:
    def student_details(self,name,age,gender):
        print(name,age,gender)

    @staticmethod
    def mentor_class(mentor_list):
        print(mentor_list)
    def mentor_details(self,mentor_list):
        print(mentor_list)

pw.mentor_class(["sudh","krish"])
pw=pwskills()
pw1=pwskills()


#static method using
class pwskills2:
    def student_details(self,name,age,gender):
        print(name,age,gender)
    
    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)


    @staticmethod
    def mentor_class(mentor_list):
        pwskills2.mentor_mail_id(["gautam@gmail.com","pawan@gmail.com"])
        print(mentor_list)
    
    @classmethod 
    def class_name(cls):
        cls.mentor_class(["sudhaa","krishaa"])
        print(cls)
    def mentor_details(self,mentor_list):
        print(mentor_list)
pwskills2.class_name()
