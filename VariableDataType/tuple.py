'''
1. In tuple we can store homogeneous data as well as heterogenous data
2. can store duplicates
3. Ordered collection of data
4. Immutable -once we declared the tuple we cannot modify it'''

t1 = (10, 45.6, True, "kodnest",10)
print(t1)

#t1.append(400)--cannot add the element to the tuple
# t1.remove(55)--cannot remove the element from the tuple
# t1.pop()--cannot poo the element from the tuple
# del t1[2]--cannot delete the element from the tuple

print(t1[2])
del t1  #deletes complte tuple
#print(t1)  #gives error after deleting

t1 = (1,2,3)
t2 = (4,5,6)
t3 =t1+t2
print(t3)