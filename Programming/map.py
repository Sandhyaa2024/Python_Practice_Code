#map accepts 2 parameter
#map function applies a given function to each item of an iterable (such as a list or tuple)
# map(function, iterable_object)

def double(x):
    return x * 2

l1 = [1,2,3,4,5]
# double method will call for each of the list l1
result = list(map(double, l1))
print(result)

print("--------------------------------")
# converting string value of tuple into integer using map
t1 = ('10','20','30')
print(t1)
t1 = tuple(map(int, t1))
print(t1)

print("--------------------------------")
# converting integer value of list into float using map
l2 = [1,5,66]
print(l2)
l2 = list(map(float,l2))
print(l2)