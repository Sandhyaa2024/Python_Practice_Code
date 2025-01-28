print("Method chaining is the proceess of Calling one method from another method")

class GrandParent:
    def disp(self):
        self.x = 100
        print(self.x)

class Parent(GrandParent):
    def disp(self):
        super().disp() #instead of this
        self.y = 200
        print(self.y)
        

class Child(Parent):
    def disp(self):
        super().disp()
    #or super(Parent, self).disp()  -- invokes the parent of 'Parent' class
        self.z = 300
        print(self.z)
        

c = Child()
c.disp()
