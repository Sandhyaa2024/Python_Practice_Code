print("To achive encapsulation getter and setter method is needed")
class Demo1:
    def __init__(self,name):
        self.__name  = name #private variable

    def getName(self):  #getter method
        return self.__name
    
    def setName(self,newName):  #setter method
        self.__name = newName

d1 = Demo1("Akash")
#print(d1.__name)  # gives error 
print(d1.getName())
d1.setName("Pooja")
print(d1.getName())