#Strings are immutable: Once we declare the string we cannot modify
#If we try to modify, then it will create new String 
#python internally uses string Interning
s1 = "Kodnest"
s1.upper()
print(s1)   #Output: Kodnest

##to get address of the K
string1 = 'K'
print(string1, id(string1))
a = 'Hello'
b = 'World'
print(a, id(a))
print(b, id(b))


'''Strng Interning is the process of checking string Intern Pool Before creating the any new Object
 whenever we create the new object , Python first will check string intern pool ,whether that object already exist or not.
 When object alreay exist in the string intern Records the address of the existing object willbe reused.'''
#fetching address of the perticular elements for the string
print("(Hello)a id of H: ", id(a[0]))
print("(Hello)a id of e: ", id(a[1]))
print("(Hello)a id of l: ", id(a[2]))  #address of l is same for all l
print("(Hello)a id of l: ", id(a[3]))   #address of l is same for all l
print("(Hello)a id of o: ", id(a[4]))   #address of o is same
print("(World)b id of l: ", id(a[3]))   #address of l is same for all l
print("(World)b id of o: ", id(a[1]))   #address of o is same


#fetching the perticular elements for the string
print(s1[0])  #Output: K
print(s1[-1])  #Output: t

#fetching address of the perticular elements for the string
print("(Kodnest)Id of K: ",id(s1[0]))
p = 'k'
print("Id of k: ", id(p))
print("(Kodnest)Id of t: ",id(s1[-1]))

