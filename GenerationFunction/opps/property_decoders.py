class pwskills:
    def __init__(self,course_price,course_name):
        self.__course_price=course_price
        self.course_name=course_name
    @property
    def course_price_access(self):
        return self.__course_price

    @course_price_access.setter
    def course_price_(self,price):
        if price<=3500:
            pass
        else:
            self.__course_price=price
    @course_price_access.deleter
    def delete_course_price(self):
        del self.__course_price 
pw=pwskills(3500,"data science master")
print(pw.course_price_access)
pw.course_price_set=4500
print(pw.course_price_access)
del pw.delete_course_price
print(pw._pwskills__course_price) 
print(pw.course_name) 