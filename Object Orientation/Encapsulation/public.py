print("The variables which are public can be accessed inside the class, outside of any class, inside the child class, inside non-child class.")


class Demo1:
    def __init__(self,name):
        self.name = name

    def disp1(self):
        print("Hello, my name is", self.name)

d1 = Demo1("Akash")
print(d1.name)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print("Hello, my name is", self.name)

d2 = Demo2("Pooja")
print(d2.name)
d2.disp2()
    