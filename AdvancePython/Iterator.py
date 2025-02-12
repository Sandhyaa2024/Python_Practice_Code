l1 = [10,20,30,40]
print(type(l1))
print(l1)
l2 = iter(l1)
print(type(l1))
print(l1) #prints iterator object memory address
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
#print(next(l2))    --StopIteration error will occure

 