def sum(a,b):
    return a+b

try:
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a number: "))
except ValueError:
    print("You entered an incorrect Value. Please enter a number")
else:
    print("sum is", sum(a,b))


    
    
try:
    c = int(input("Please enter a number: "))
    print(5/c)
except ValueError:
    print("You entered an incorrect value. Please enter a number")
except ZeroDivisionError:
    print("Number can't divide to zero. Please enter a different number")



def sum(a,b):
    return a+b
    
try:
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a number: "))
except ValueError:
    print("You entered an incorrect value. Please enter a number. ")
else:
    print("sum is", sum(a,b))
finally:
    print("process ended")




try:
    c = int(input("Please enter a number: "))
    print(5/c)
except ValueError:
    print("You entered an incorrect value. Please enter a number")
except ZeroDivisionError:
    print("Number can't divide to zero. Please enter a different number")
finally:
    print("process ended.")




def Reverse(s):
    if type(s) !=str:
        raise ValueError("You entered an incorrect value. Please enter a proper value.")
    else:
        return s[::-1]
Reverse("Python")



Reverse("7894563125")


Wrong_Character = list("$çgûïÎ&çGùø")
Password = input("Password")

for letter in Password:
    if letter in Wrong_Character:
        raise TypeError("You can't use non-English letters.")
    else:
        pass
    print("Password accepted...")