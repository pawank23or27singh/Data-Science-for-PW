def test_fibo(n):
    a,b=0,1
    for i in range(n):
        yield a  #yield is used to return value from the function
        a,b=b,a+b

for i in test_fibo(10):
    print(i)
    
# def count_test(n):
#     cout=1
#     while cout<=n:
#         yield cout
#         cout+=1
# c=cout_text(5)
#for i in c:
#   print(i) 