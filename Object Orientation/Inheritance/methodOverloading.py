#doesn't support method overloading
#so we can't have two methods with same name but different parameters
#Only last method it will access

class Demo: 
    def disp(self):
        print("Inside disp with 0 parameters")
    def disp(self, a):
        print("Inside disp with 1 parameter")
    def disp(self,a, b):
        print("Inside disp with 2 parameters")

d = Demo()
# d.disp()
# d.disp(10)
d.disp(34,89)