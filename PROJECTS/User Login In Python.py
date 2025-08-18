Sys_User_Name="Sandy"
Sys_Password="Sandy.3652"

User_Name=input("Please Enter Your Name:")
User_Password=input("Please Enter Your Password:")


if User_Name != Sys_User_Name and User_Password == Sys_Password:
    print("Wrong User Name...")

elif User_Name == Sys_User_Name and User_Password != Sys_Password:
    print("Wrong Password")

elif User_Name != Sys_User_Name and User_Password != Sys_Password:
    print("Wrong User Name And Password!")

else:
    print("Logged-In Successfully...")
