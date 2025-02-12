print("Names of error: ZeroDivisionError, NameError, TypeError, ValueError")
print("To raise the error we will use raise()")

def checkAge(age):
    if(age < 18):
        raise ValueError("Age must be greater than 18")
#checkAge(12) # output: ValueError: Age must be greater than 18

# To handle it
try:
    checkAge(8)
except ValueError as e:
    print("Error Message:",e) #output: Error Message: Age must be greater than 18