class Demo1:
    def displ(self):
        print("Inside disp1")
    
class Demo2(Demo1):
    def disp2(self):
        print("Inside disp2")

class Demo3(Demo2):
    pass


d2 = Demo2()
d2.displ()
d2.disp2()
print("------------------")
d3 = Demo3()
d3.disp2()
d3.displ()