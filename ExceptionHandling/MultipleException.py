print("default except must be present in the last")

def disp(a,b):
    try:
        print(a/b)  
        # print(a/c)  NameError
    except ZeroDivisionError:
        print("ZeroDivisionError occured and Handled")
    except NameError:
        print("NameError occured and handled")
    except TypeError:
        print("TypeError occured and handled")
    except:
        print("default except must be present in the last")  #default except must be present in

disp(10,20)
disp(10,0)
disp(10,"kod")