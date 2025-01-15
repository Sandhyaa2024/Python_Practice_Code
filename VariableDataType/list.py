''''------------------------Features of list-------------------
1.Can store homogeneous as well as heterogeneous data.
2.Can store duplicate values.
3.Its an ordered collection odf data. i.e order of insertion will remain as it is in the output.
4. List are mutable- once we declare we can modify it.'''

l1 = [10,20,30,40,44.09,True, "string",20]
print(l1, type(l1))

print(l1[2])  # access value which is present in index 2
print(l1[-1])  # access value which is present at last index

#append() will add element at the end of the list
l1.append(64.90)
print(l1)

#insert(index,element)---- will add at specific position
l1.insert(1,15)
print(l1)

#remove(value)   - will remove the first occurrance specific elements 
l1.remove(20)
print(l1)

#l1.discard(2000)    #if element is not present in the list gives error

# in and not in operator
print(20 in l1)  # returns true if element is present in the list
print(2000 not in l1)  # returns true if element is not present in the list

#pop() - without argument will delete an dreturn last element from list
removed_ele = l1.pop()
print(removed_ele)
print(l1)

#pop(index) - with argument will delete the element at specific index
removed_ele = l1.pop(1)
print(removed_ele)
print(l1)

'''remove takes values as argument but pop takes index as argument
pop returns removed value but remove will not return value'''

