"""
1.can store both homogenous as well as heterogenous data
2.unordered collection of data - (does not support indexing of)
3.cannot store duplicates
4.sets are mutable 
"""


s1= {10,True, "Kodnest", 45.78,10}
print(s1, type(s1)) #output: {True, 10, 45.78, 'Kodnest'}

#print(s1[0]) -- error does not support indexing 

#functions:
#1.add() - add element to set
s1.add(500)
print(s1) #output: {True, 10, 45.78, 'Kodnest',500}

#2.remove() - remove element from set
s1.remove(10)
print(s1)

#3. pop() without index returns and deletes random element
print(s1.pop())
print(s1)