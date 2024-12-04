import threading
def test(id):
    print("Prog start %d " % id)

test(54)
thread=[threading.Thread(target =test,args=(i,))for i in range(10)]
for t in thread:
    t.start()
print(thread)
print(id(thread))
