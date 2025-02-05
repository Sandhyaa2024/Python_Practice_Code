print("1. NameMangling is the process of providing new name to the private variables")
print("2.These new names will be provided automatically by pyhton for all private members.")
print("3.New will be provided in the formate: \n'objectName._className__variableName'")

class Demo1:
    def __init__(self,name):
        self.__name  = name #private variable


#getter and setter method is not efeicient in python so we have NameMangling
d1 = Demo1("Akash")
print(d1._Demo1__name)  #achiving NameMangling
