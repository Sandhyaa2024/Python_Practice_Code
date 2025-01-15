#Square star pattern 5 rows 5 colonms
rows = 5
col = 5
for i in range(rows):
    for j in range(col):
        print("*", end = " ")
    print()


print()
#right angle triangle
for i in range(0,rows):
    for j in range(i+1):
        print("*", end = " ")
    print()


print()
for i in range(rows):
    for j in range(rows - i):
        print("*", end = " ")
    print()





#Right pascle triangle
print()
for i in range(0,rows):
    for j in range(i+1):
        print("*", end = " ")
    print()
for i in range(rows):
    for j in range(rows - i-1):
        print("*", end = " ")
    print()



#Butterfly Pattern
print()
for i in range(rows):
    for j in range(i+1):
        print("*", end = " ")
    for j in range(rows-i-1):
        print(" ", end = " ")
    for j in range(rows-i-1):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()
for i in range(rows):
    for j in range(rows-i-1):
        print("*", end = " ")
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(rows-i-1):
        print("*", end = " ")
    print()


#Daimond shape
print()
for i in range(rows):
    for j in range(rows-i-1):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()
for i in range(1,rows):
    for j in range(i):
        print(" ", end = " ")
    for j in range(rows-i-1):
        print("*", end = " ")
    for j in range(rows-i):
        print("*", end = " ")
    print()


    