class Demo1:
    def disp1(self):
        print("Inside disp1")
    
class Demo2:
    def disp2(self):
        print("Inside disp2")

class Demo3(Demo1, Demo2):
    pass

d3 = Demo3()
d3.disp1()
d3.disp2()


# when methods having same name 
print("--------------------------------------------------------- ")
print("This is MRO technique- 1st child class is checked for the method then parent classes will be searched")
#Not method overriding
class Demo1:
    def disp(self):
        print("Inside disp1")

class Demo2:
    def disp(self):
        print("Inside disp2")
#parent class searched from left to right, if found stop searching
class Demo3(Demo1,Demo2):
    pass

d = Demo3()
d.disp()    #output:- Inside disp1


print("--------------------------------------------------------- ")
class Demo1:
    def __init__(self):
        self.x = 100
class Demo2:
    def __init__(self):
        self.x = 200
class Demo3(Demo2, Demo1):
    def __init__(self):
        self.x = 300
#MRO is used to find the attribute
dd3 = Demo3()
print(dd3.x) #output:- 300

