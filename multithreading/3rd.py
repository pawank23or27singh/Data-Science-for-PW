import time
import threading
def test1(id):
    for i in range(10):
        print("test1 %d printing %d %s" %(id,i,time.ctime()))
        time.sleep(0)
test1(0)
thread1=[threading.Thread(target =test1,args=(i,))for i in range(3)]
for t in thread1:
    t.start()
