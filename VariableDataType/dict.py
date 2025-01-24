
""" key name canno"""
d1 = {'name': 'abc','age': 27,'phone':23456543}
print(d1,type(d1))

d1['name'] = "abc"
print(d1)

d1['name'] = "XYZ"
print(d1)

#unpacking of dictionary
d = {10:2,20:1,30:1}
for key, value in d.items():
    print(f"{key} occures {value} time(s)")