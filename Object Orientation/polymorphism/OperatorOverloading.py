class Demo1:
    def disp1(self):
        print("Inside disp 1")

    def __str__(self):
        return "Demo1 Class"
    
    def __add__(self,other):
        self.a = 20
        other.b = 30
        return self.a + other.b

class Demo2:
    def disp2(self):
        print("Inside disp 2")

    def __str__(self):
        return "Demo2 Class"
    
    

d1 = Demo1()
d2 = Demo2()

print("In Python if we print reference variable then internally python will invoke __str__() which always return string reperesentation of an address of an object")

#In above example we have overridden __str__ method in their respective classes

print(d1)
print(d2)

#concatenation cannot be done
print(d1+d2)