#String validators:
# 1.alnum()
# 2.alpha()
# 3.isdigit()
# 4.islower()
# 5.isupper()
# 6.any()



#1.    alnum()  :-To check only numbers or only alphabets or both alphabets and numbers
s = 'Kodnest'
print(s.isalnum()) #True

s1 = "kodgf4453*"
print(s1.isalnum()) #False

s2 = "dfgrtf"
print(s2.isalnum()) #True


#2.  alpha()    :- For only alphabets
s3 = "gfhghdj12"
print(s3.isalpha()) #False


#3.  isdigit()  :- checks only digits are present
s4 ="12345"
print(s4.isdigit()) #True


#4.  islower()   :-checks all alphabets are lowercase
s5 = "kodnest"
print(s5.islower()) #True


#5.  isupper()   :-checks all alphabets are uppercase
s6 = "Kodnest"
print(s6.isupper()) #Flase


#6.  any()      :-checks any character is present or not6.   any()   :- checks any character is present or not or only one value shoud be true then it will give True
s7 = (True,False,False)
print(s7.any()) #True

s8 = (False,False)
print(s8.any()) #False

#--------------------------Example-------------------
str = input() #qA!
print(any([i.isalnum() for i in str])) 
print(any([i.isalpha() for i in str]))
print(any([i.isdigit() for i in str]))
print(any([i.isupper() for i in str]))
print(any([i.islower() for i in str]))