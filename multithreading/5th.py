
# multiprocessing
import multiprocessing
import multiprocessing.pool
def test():#Child process
    print("this is my Multiprocess")

if __name__=="__main__":#main function
    m=multiprocessing.Process(target=test)
    print("This is my main process")
    m.start()
    m.join()


# multiprocessing me pool function use krne ke liye 
def ssqure(n):
    return n**2
if __name__=="__main__":
    with multiprocessing.pool.Pool(processes=4) as pool:
        out=pool.map(ssqure,[1,2,3,4,5,6,7,8,9,10])
        print(out) 


# another wayto acchive multiprocessing

def producer(q):
    for i in range(10):
        q.put(i)

def consumer(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(item)

if __name__=="__main__":
    queue=multiprocessing.Queue()
    p=multiprocessing.Process(target=producer,args=(queue,))
    c=multiprocessing.Process(target=consumer,args=(queue,))
    p.start()
    c.start()
    p.join()
    c.join()
    queue.put("None")
    queue.close()


# another wayto acchive multiprocessing

def square(index,value):
    value[index]=value[index]**2
if __name__=="main__":
    arr=multiprocessing.Array('i',[1,2,3,4,5,6,7,8,9,10])   
    process=[]
    for i in range(10):
        p=multiprocessing.Process(target=square,args=(i,arr))
        process.append(p)
        p.start()
    for p in process:
        p.join()
    print(list(arr))

# pipe

import multiprocessing
def sender(conn,msg):
    for i in msg:
        conn.send(i)
    conn.close()

def receiver(conn):
    while True:
        try:
            message=conn.recv()
        except Exception as e:
            print(e)
            break
        print(message)

if __name__=="__main__":   
    msg=["my name is pawan","i am from patna","i love coding"]
    parent_con,child_con=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=sender,args=(child_con,msg))
    p2=multiprocessing.Process(target=receiver,args=(parent_con,))
    p1.start()
    p2.start()
    p1.join()
    child_con.close()
    p2.join()
    parent_con.close()
print(msg)
