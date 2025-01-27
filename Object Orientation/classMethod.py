class Student:
    college_name = "Kodnest"

    def getInfo(self):
        print(f"College name is {self.college_name}")

    @classmethod
    def change_name(cls, new_name):
        cls.college_name = new_name


s = Student()
s.getInfo()     #Output: College name is Kodnest
s.change_name("Code")
s.getInfo()  # Output: College name is Code
