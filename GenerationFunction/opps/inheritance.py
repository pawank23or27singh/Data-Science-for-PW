class test:
    def test_meth(self):
        return "this is my first class"
class child_test(test):
    pass
child_test_obj=child_test()
print(child_test_obj.test_meth())


#multiple inheritance
class class1:
    def test_class1(self):
        return "this is meth from class1"
class class2(class1):
    def test_class2(self):
        return "this is meth from class2"
class class3(class2):
    pass
obj_class3=class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())


#method overriding
class class1:
    def test_class1(self):
        return "this is meth from class1"
class class2:
    def test_class2(self):
        return "this is meth from class 2"
class class3(class1,class2):
    pass
obj_class3=class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())