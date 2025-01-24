l1 = [10,5,3,20]
#sort in accending order
l1.sort()
print(l1) #sorts the original list

#sort in accending but prints in decending order
l1.sort(reverse=True)
print(l1)

print("------------------------------")
l2 = [100, 30,500,10]
#first have to assign to a new list becuase its not posible to change the original list l2
sorted_l2 = sorted(l2)
print(sorted_l2)