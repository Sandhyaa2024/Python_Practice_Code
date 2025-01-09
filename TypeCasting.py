#if string is holding integer then is can be converted into integer
a = "30"
print(a, type(a))
b = int(a)
print(b, type(b))

#String to integer conversion is not allowed
x="Kod"
print(x, type(x))
# y = int(x)
# print(y, type(y))

p = float(input("Enter float type of data: "))
print(p, type(p))

# bool()  method
# bool() method returns True if the value is not zero and not None
# bool() method returns False if the value is zero or None
# bool() method returns False if the value is empty string

q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))
r = 0
r = bool(r)
print(r, type(r))
s = ''
s = bool(s)
print(s, type(s))

#Taking float value from user and converting it into int
value = int(float(input("Enter price: Float value ")))
print(value, type(value))