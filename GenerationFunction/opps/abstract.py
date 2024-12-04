import abc
class pwskills:
    @abc.abstractmethod
    def students_details(self):
        pass
    @abc.abstractmethod
    def teacher_details(self):
        pass
    @abc.abstractmethod
    def students_marks(self):
        pass
class pwskillsinfo(pwskills):
    def students_details(self):
        return "this is student details about data science"
    def teacher_details(self):
        return "this is teacher details about data science"
class data_science(pwskills):
    def students_marks(self):
        return "this is student marks in data science"

obj=data_science() 
print(obj.students_marks())
print(obj.students_details())
print(obj.teacher_details())

         