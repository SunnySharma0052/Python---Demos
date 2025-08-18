from random import randrange

nums_per_letter = 1

def createCard():
    card = {}
    lower = 1
    upper = 1 + nums_per_letter

    for letter in["B", "I", "N", "G", "O"]:
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
            if next_num not in card[letter]:
                card[letter].append(next_num)

            lower = lower + nums_per_letter
            upper = upper + nums_per_letter
    return card

def displayCard(card):
    print(" B  I  N  G  O ")
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d "% card[letter][i], end = "")
        print()

def main():
    card = createCard()
    displayCard(card)

if __name__=="__main__":
    main()