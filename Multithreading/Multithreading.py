import threading
import time
print(threading.current_thread())

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

def disp1(l1):
    print(threading.current_thread())
    for i in l1:
        print(i)
        time.sleep(2)

def disp2(l2):
    print(threading.current_thread())
    for i in l2:
        print(i)
        time.sleep(1)


t1 = threading.Thread(target = disp1, args =(l1,), name ="Tester")
t2 = threading.Thread(target = disp2, args =(l2,), name = "Developer")


t1.start()
t1.join()
print(t1.is_alive())
t2.start()