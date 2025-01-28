print("Inherited method: method inherited from parent class and used as it is. ")
print("Overriden method: method inherited from parent class and  modified as child requirement(changs the body).")
print("Specialized method: method only presented in child class")

class Student:
    def cook(self):
        print("Student is cooking")
    def play(self):
        print("Student is playing")

class Employee(Student):
    def work(self):
        print("Employee is working")
    def cook(self):
        print("Employee is cooking")

e = Employee()
e.play()