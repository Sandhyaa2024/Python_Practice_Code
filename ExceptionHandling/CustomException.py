class PinError(Exception):  #syntax to create a user exception
    pass

correctPin = 1234
pin = int(input("Enter 4 digit PIN: "))
try:
    if(pin == correctPin):
        print("Access Granted")
    else:
        raise PinError("Pin is not correct")
except PinError as p:
    print("Incorrect Pin: ", p)