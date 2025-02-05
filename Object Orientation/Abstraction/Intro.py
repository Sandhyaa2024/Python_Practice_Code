from abc import ABC, abstractmethod
class Demo1:
    @abstractmethod
    def disp3(self):
        pass

class Demo2(Demo1):
    def info(self):
        print("Inside info")

    
    def disp3(self):
        print("Inside disp3")

class Demo3(Demo2):
    pass

d4 = Demo3()
d4.info()