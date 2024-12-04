# def deco(func):
#     def inner_deco():
#         print("this is the start of the function")
#         func()
#         print("this is the end of function")
#         return inner_deco
#     @deco
#     def test1():
#         print(6+7)
#     print(test1())

#decorator
import time
def timer_test(func):
    def timer_test_inner():
        start=time.time()
        func()
        end=time.time()
        print( end -start)
    return timer_test_inner    
def test2():
    print(5+6)
print(timer_test(test2))
print(test2())
@timer_test
def test3():
    print(78+98)
print(timer_test(test3))
print(test3())    

