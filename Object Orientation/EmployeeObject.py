class Employee:
    company_name = "code"
    def __init__(self, name, age, desig):
        self.name = name
        self.age = age
        self.desig = desig
    
    def getDetail(self):
       print(f"Name: {self.name}, Age: {self.age}, Designation: {self.desig}")
    
    def login(self, time):
        print(f"{self.name} logged in at {time}")

    def logout(self, time):
        print(f"{self.name} logged out at {time}")

    def work(self, hours):
        print(f"{self.name} worked for  {hours}")

e1 = Employee("abc",25,"SDE")
e2 = Employee("xyz",24,"Sales")
e3 = Employee("pqr",26,"Developer")
e1.getDetail()
e2.getDetail()
e3.getDetail()
e1.login("9:00")
e1.logout("17:00")
e1.work(8)

e2.login("4:00")
e2.logout("19:00")
e2.work(8)

e3.login("4:00")
e3.logout("18:00")
e3.work(9)