print("1. try block: Used to keep the logic in which we may get some error.")
print("2. except block: will be executed when execption occured in try block logic.")
print("3. else block: will be executed when try block logic will be executed without any error")
print("4. finally block: will be always executed irrespective of execption occured or not.")

def disp1(a,b):
    try:
        print("Task started.")
        print(a/b)
    except:
        print("Error: Division by zero is not allowed.")
    else:
        print("Task completed successfully without execption.")
    finally:
        print("Task finished.")

disp1(10,0)
disp1(15,5)
disp1(10,3)
