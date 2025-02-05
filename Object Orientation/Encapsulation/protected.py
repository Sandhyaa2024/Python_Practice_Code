print("The variables which are public can be accessed inside the class, outside of any class, inside the child class, inside non-child class.")
print("The variables which are protected should be accessed inside same class and inside child class and this is programmer duty to follow these rules.")


class Demo1:
    def __init__(self,name):
        self._name = name

    def disp1(self):
        print("Hello, my name is", self._name)

d1 = Demo1("Akash")
print(d1._name)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print("Hello, my name is", self._name)

d2 = Demo2("Pooja")
print(d2._name)
d2.disp2()

class Demo3:
    def disp3(self):
        print(d1._name)
d3 = Demo3()
d3.disp3()