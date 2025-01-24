# 1st way of taking user input for the list
# using for loop
l1 = []
n = int(input("Enter the number of elements:"))
for i in range(0, n):
    elements = int(input(f"Enter the element at index {i}:"))
    l1.append(elements)
print(l1)
print("------------------------------")

# 2nd way of taking user input for the list
# using split()
l2 = input("Enter space seperated elements:")
print(l2,type(l2))
l2 = l2.split()
print(l2,type(l2))
print("------------------------------")

# 3rd way of taking user input for the list
# using map() function
l3 = list(map(int, input("Enter space seperated elements:").split()))
print(l3,type(l3))
print("------------------------------")

# 1st way of taking user input for the tuple
# using map() function
t3 = tuple(map(int, input("Enter space seperated elements:").split()))
print(t3,type(t3))
print("------------------------------")

li = list(map(int,input().split()))
print([i for i in li if i%2 == 0])
