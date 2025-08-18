# Letter Counter In Python Hand-ON

string = "India is most beautiful cities in the world"

Frequency = dict()

for character in string:

    if character in Frequency:

        Frequency[character] += 1
    
    else:

        Frequency[character] = 1

for letter, count in Frequency.items():

    print(letter, ":", count)
