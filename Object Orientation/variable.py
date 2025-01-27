class Bank:
    bank_name = "XYZ"
    def __init__(self, name, age, bal):
        self.name = name
        self.age = age
        self.bal = bal

    def get_info(self):
        print(f"""User Name: {self.name} and ,
User Balance: {self.bal} for 
Bank: {Bank.bank_name} """)

b1 = Bank("Abhi",26,55000)

print(b1.bank_name)     #Can access the static or class variable using object 
print(Bank.bank_name)
b1.get_info()
