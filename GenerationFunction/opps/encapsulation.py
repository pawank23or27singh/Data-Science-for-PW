#encapsulation is the process of wrapping data and code in a single unit to hide it from other classes and functions without changing it as it is privately accessible to the class
class car:
    def __init__(self,year,make ,model,speed):
        self.__year=year# double under score is a private variable
        self.__make=make
        self.__model=model
        self.__speed=0
    def set_speed(self,speed):
        self.__speed=0 if speed <0 else speed
    def get_speed(self):
        return self.__speed
c=car(2021,"audi","a4",12)
print (c._car__year)
print(c.set_speed(344))
print(c.get_speed())
