BABY_PRICE = 0.00
CHILD_PRICE = 10.00
ADULT_PRICE = 20.00
SENIOR_PRICE = 16.00

BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

total = 0

line = input("Enter the age of the guest(blank to finish): ")
while line !="":
    age = int(line)
    if age <= BABY_LIMIT:
        total = total + BABY_PRICE
    elif age <= CHILD_LIMIT:
        total = total + CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total = total + ADULT_PRICE
    else:
        total = total + SENIOR_PRICE
    line = input("Enter the age of guest(blank to finish): ")
print("The total for that group is $%.2f" % total)
