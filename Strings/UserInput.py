#Input method will always takes the input as String
num1 = input("Enter the Number 1:")
print(f'Value of num1 is: {num1}, Data Type of num1 is {type(num1)}')

#Taking User input as Integer
num2 = int(input("Enter a number 2:"))
print(f'Value of num2 is: {num2}, Data Type of num2 is {type(num2)}')

#Operations of 2 numbers
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print(f'Addition of {a} and {b} is: {a+b}')     #30
print(f'Subtraction of {a} and {b} is: {a-b}')  #10
print(f'Multiplication of {a} and {b} is: {a*b}')   #200
print(f'Division of {a} and {b} is: {a/b}')     #2.0 (Division result will always be of type float)