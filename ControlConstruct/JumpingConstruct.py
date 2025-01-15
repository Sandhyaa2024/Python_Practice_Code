#---------------------------Continue----------------------------------------------------
#WAP to print numbers fro 1 to 10 but if number is 6 then skip printing
for i in range(1,11):
    if i == 6:
        continue
    else:
        print(i, end =" ")
print()


#--------------------------------------break---------------------------------------------
#WAP to print numbers from 1  but stop as soon as number is 6
for i in range(1,11):
    if i == 6:
        break
    print(i, end =" ")
print()

# ----------------------------------pass---------------------------------------------
#helpful when your writing draft of your code
for num in range(1,4):
    if num == 2:
        pass