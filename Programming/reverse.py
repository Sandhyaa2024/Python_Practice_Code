# reverse() method will reverse the original method
li = [10,5,20,7,40]
print("Before reverse:",li)
li.reverse()
print("After reverse:",li)

print("------------------------------")
#reversed(object)
l2 = [10,5,20,7,40]
print("Before reverse:",l2)
reversed(l2) # this will reverse the list
print(l2) # But this prints same list because it has to be assigned to new list
revl2 = reversed(l2)
print("After reverse:",list(revl2)) # Now it prints reversed list


print("------------------------------")
l3 = [1,5,2,9]
print("Before reverse:",l3)
l3.reverse() # This will reverse the list in place
print("After reverse:",l3) # This will print same list because it has to b
# assigned to new list
new_l3 = reversed(l3)
print(new_l3) # This will print reversed list