def disp():
    return 10
    return 20
    return 30

print(disp())   # output 10
print(disp())   # output 10
print(disp())   # output 10
print("---------------------------")
#______________Usinf generator method____________________


#if yield is present inside the function then it is generator function
def generator_function():
    yield 10
    yield 20
    yield 30

print(generator_function())
g = generator_function()
print(next(g))   # output 10
print(next(g))  # output 20
print(next(g))   # output 30
print(next(g))


