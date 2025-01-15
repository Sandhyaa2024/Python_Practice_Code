#--------------------------------For loop-----------------------------
#Syntax: for control_variable in iterable_object
#Example: for i in range(5):

for i in 'Kodnest':
    print(i, end=" ")
print()

for j in [10,30,50,70]:
    print(j+5, end=" ")
print()

for num in range(1,11): #prints 1 to 10
    print(num)
print()

#range in for loop
for i in range(11,21,2):
    print(i, end = " ")
print()

#write program to print even numbers from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i,end=" ")
print()

#---------------------------------while loop--------------------------------------------
#Syntax: while condition: while condition:
i=0 
while i<5: 
    i=i+1 
    print(i,end = " ")
print()

