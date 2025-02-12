import threading
import time
print(threading.current_thread())

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

def disp1(l1):
    for i in l1:
        print(i)
        time.sleep(1)

def disp2(l2):
    for i in l2:
        print(i)
        time.sleep(1)

disp1(l1)
disp2(l2)