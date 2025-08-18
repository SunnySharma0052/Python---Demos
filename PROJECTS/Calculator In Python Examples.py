import math

print("""

1)  Addition
2)  Subtraction
3)  Multiplication
4)  Division
5)  Exponent
6)  Calculat BMI
7)  Calculate The Area Of Triangle
8)  Calculate The Area Of Square
9)  Finding The Square Root
   For exit press 0

   """)

operation=int(input("Please Choose Operation You Want To Do:"))

if operation ==1:
    number_1=int(input("Please Enter The First Number:"))
    number_2=int(input("Please Enter The Second Number:"))

    print("Result:",number_1+number_2)


elif operation ==2:
    number_1=int(input("Please Enter The First Number:"))
    number_2=int(input("Please Enter The Second Number:"))

    print("Result:",number_1-number_2)


elif operation ==3:
    number_1=int(input("Please Enter The First Number:"))
    number_2=int(input("Please Enter The Second Number:"))

    print("Result:",number_1*number_2)


elif operation ==4:
    number_1=int(input("Please Enter The First Number:"))
    number_2=int(input("Please Enter The Second Number:"))

    print("Result:",number_1/number_2)


elif operation ==5:
    number_1=int(input("Please Enter A Number:"))

    print("Result",number_1**2)


elif operation ==6:
    Height=float(input("Please Enter Your Height In Meter:"))
    Weight=int(input("Please Enter Your Weight:"))
    Gender=str(input("Please Enter Your Gender:"))
    
    print("BMI:",Weight/Height**2)


elif operation ==7:
    Base=int(input("Please Enter The Base:"))
    Height=int(input("Please Enter The Height:"))

    print("Result:",(Base*Height)/2)


elif operation ==8:
    side=int(input("Please Enter The Side:"))

    print("Result:",side*side)


elif operation ==9:
    number=int(input("Please Enter A Number:"))

    print("Result:",number**2)


elif operation ==0:
    print("Programm Is Shutting Down...")


else:
    print("Invalid Operation...")
