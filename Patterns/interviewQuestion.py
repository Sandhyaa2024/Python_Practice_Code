for y in range(1,11):
    z = 200

def  display(a):
    print(a)
    y= 100  #this is local variable so cannot access in line 10
    print(y)

display(50)
print(y)  # for loops y value will be stored i.e 10
print(z)
#print(a)   -error



