import random
from enum import Enum
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True
while playagain:
    playerchoice = input("Enter...\n1 For Rock,\n2 For Paper,\n3 For Scissors:\n")
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("You must enter a number 1, 2, or 3.")
    computerchoice = random.choice("123")
    computer = int(computerchoice) 
    # str(RPS(player)).replace("RPS.","")
    print("You choose " + playerchoice + ".")
    print("Python choose " + computerchoice + ".")
    print("")
    if player == computer:
        print("🤜🤛 Tie")
    elif player == 1 and computer == 3:
        print("✌️ 🥳You win")
    elif player == 2 and computer == 1:
        print("✌️ 🥳You win")
    elif player == 3 and computer == 2:
        print("✌️ 🥳You win")
    else:
        print("🤬🤬Python wins")
    playagain = input("\nDo you want to play again? \nY for yes, N for no: ")
    if playagain.lower() == "y":
        continue
    else:
        print("Thanks for playing!")
        playagain = False
