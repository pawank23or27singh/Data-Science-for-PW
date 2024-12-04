import os
import threading
import time
shared_var=0
lock_var=threading.Lock()
def test2(id):
    global shared_var
    with lock_var:
        shared_var+=1
        print("test2 is %d has increase the shared variable by %d" %(id ,shared_var))
        time.sleep(1)
tread3=[threading.Thread(target =test2,args=(i,))for i in range(3)]
for t in tread3:
    t.start()