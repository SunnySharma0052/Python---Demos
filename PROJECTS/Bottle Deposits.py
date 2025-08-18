Less_deposit =0.12
More_deposit = 0.27

less = int(input("How many containers 1 liter or less? : "))
more = int(input("How many containers more than 1 liter? : "))

refund = less * Less_deposit + more * More_deposit
print("Your total refund will be $%.2f."% refund)