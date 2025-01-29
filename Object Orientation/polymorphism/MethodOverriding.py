print("Polymorphism:- somthig which exhibits meny form")
print("one method perform multiple task")

class Calculator:
    def calculate(self,a,b):
        print("Calculates result of a and b")

class add(Calculator):
    def calculate(self,a,b):
        print("Addition:",a+b)

class sub(Calculator):
    def calculate(self,a,b):
        print("Subtraction:",a-b)

class mul(Calculator):
    pass


ref = add()
ref.calculate(5,6)  #11
ref = sub()
ref.calculate(15,6)   #9
ref = mul()
ref.calculate(10,20)




    