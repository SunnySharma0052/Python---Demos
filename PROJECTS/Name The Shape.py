Num_sides = int(input("Enter the number of sides: "))

name = ""
if Num_sides == 3:
    name = "triangle"
elif Num_sides == 4:
    name = "quadriliateral/square"
elif Num_sides == 5:
    name = "pentagon"
elif Num_sides == 6:
    name = "hexagon"
elif Num_sides == 7:
    name = "heptagon"
elif Num_sides == 8:
    name = "octagon"
elif Num_sides == 9:
    name = "nonagon"
elif Num_sides == 10:
    name = "decagon"

if name == "":
    print("That number of sides is not supported by this program.")
else:
    print("That's a", name)
