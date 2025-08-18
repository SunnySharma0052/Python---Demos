data = []
num = int(input("Enter an integer(0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter an integer(0 to quit): "))
data.sort()
print("The value, sorted into ascending order, are: ")
for num in data:
    print(num)