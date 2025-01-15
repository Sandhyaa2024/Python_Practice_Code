'''
1. Conditional : if, if-else, if-elif
2. Looping : for, while
3. Jumping : break, continue, pass
'''

def checkAge(age):
    if (age > 18):
        print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

#WAP to display 'child' if age is below 18, display 'adult' if age is above 18, ifage is above 65 display 'senior citizen'
def checkAgeCategory(age):
    if(age < 18):
        print("Child")
    elif (age >=18 and age <=65):
        print("Adult")
    else:
        print("Senior Citizen")
age = int(input("Enter age: "))
checkAgeCategory(age)