
class add:
    def calculate(self,a,b):
        print("Addition:",a+b)

class sub:
    def calculate(self,a,b):
        print("Subtraction:",a-b)

class mul:
    pass

print("----------Duct typing----------------") 
#instead of above 4 lines(17,18,19,10) we can use this like this
print("1.ref won't check the type of object\n2.ref only gives the importance to the calculate methos\n3. give imporatnce to the methods of object ")
def permit(ref,a,b):
    if type(ref).__name__=="mul":
        print("Mul class does not have calculator() ")
    else:
        ref.calculate(a,b)
permit(add(),5,6)
permit(sub(),15,6)
permit(mul(),10,4)
