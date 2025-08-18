Sys_User_Name="Sandy"
Sys_Password="Sandyyy.3652"

Attempts = 3

while True:
    User_Name=str(input("Please Enter Your User Name:"))
    User_Password=input("Please Enter Your User Password:")

    if User_Name != Sys_User_Name and User_Password == Sys_Password:
        print("Wrong User Name...")
        Attempts -=1

    elif User_Name == Sys_User_Name and User_Password != Sys_Password:
        print("Wrong User Password...")
        Attempts -=1

    elif User_Name != Sys_User_Name and User_Password != Sys_Password:
        print("Wrong User Name and Password...")
        Attempts -=1

    else:
        print("Logged-In Successfully")
        break

    if Attempts == 0:
        print("You No Longer Have Access.Please Contact Your System Manager")
        break
