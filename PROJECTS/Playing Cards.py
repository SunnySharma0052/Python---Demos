from random import randrange

def createDeck():
    cards = []
    for suit in["s","h","d","c"]:
        for value in["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
            cards.append(value + suit)
    return cards

def shuffle(cards):
    for i in range(0,len(cards)):
        other_position = randrange(i,len(cards))
        Temp = cards[1]
        cards[i]=cards[other_position]
        cards[other_position] = Temp
def main():
    cards = createDeck()
    print("The original deck of cards is: ")
    print(cards)
    print()
    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)

if __name__ == "__main__":
    main()