import random
import time
print("""
      
    Rock-Paper-Scissors Game
      
    Please choose one of them
      
    1-Rock
    2-Paper
    3-Scissors
    4-Exit Game
      
    Rules
      
    1-Rock beats scissors
    2-Scissors beats paper
    3-Paper beats rock
      
    Have fun!
      
    """)

while True:

    User_1 = int(input("Your Choose: "))

    if User_1 == 4:
        print("Game Over!")
        break

    elif User_1 >= 5:
        print("Please Choose 1 to 4!")

    else:

        Game = {1:"Rock", 2:"Paper", 3:"Scissors"}

        AI_1 = random.randint(1,3)

        AI = Game.get(AI_1)
        User = Game.get(User_1)

        if User == "Rock" and AI == "Scissors":
            time.sleep(0.1)
            print("I choose scissors, You WIN!")

        elif User == "Rock" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, You LOSE!")

        elif User == "Paper" and AI == "Scissors":
            time.sleep(0.1)
            print("I choose scissors, You LOSE!")

        elif User == "Paper" and AI == "Rock":
            time.sleep(0.1)
            print("I choose rock, You WIN!")

        elif User == "Scissors" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, You WIN!")

        elif User == "Scissors" and AI == "Rock":
            time.sleep(0.1)
            print("I choose rock, You LOSE!")

        else:
            print("Draw. Please Continue.")
