O_List = [number for number in range(150) if number % 2 != 0]

P_List = []

for num in range (2,150):
    prime = True

    for i in range(2,num):

        if (num %1 == 0):
            prime = False

    if prime:
        P_List.append(num)

with open("odd_Number.txt", "w") as odd_Numbers:

    for number in O_List:
        odd_Numbers.write(str(number)+ ", ")

with open("Prime_Numbers.txt", "w") as  Prime_Numbers:

    for number in P_List:
        Prime_Numbers.write(str(number)+ ", ")

overlap = []

for numbers in P_List:

    if numbers in O_List:
        overlap.append(numbers)

with open("Overlap_Number", "w") as overlap_Numbers:
    for number in overlap:
        overlap_Numbers.write(str(number)+ ", ")
