import random
import sys

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess ehich number I'm thinking of... 1, 2 or 3:\n "
        )
        if playerchoice not in ["1","2","3"]:
            print(f"\n{name}, please enter 1, 2 or 3.")
            return play_guess_number()
        computerchoice = random.choice("123")
        print(f"\n{name}, you choose {playerchoice}")
        print(f"I was thinking about the number {computerchoice}")

        player = int(playerchoice)
        computer = int(computerchoice)
        
        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"🥳{name} wins!"
            else :
                return f"🤬🤬 Sorry, {name}. Better luck next time!"

        game_result = decide_winner(player,computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"{name} wins: {player_wins}")
        print(f"\nYour winning percentage is {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")
        while True:
            play_again = input("\nY for Yes or \nN for No: ")
            if play_again.lower() not in ["y","n"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_guess_number()
        else :
            print("\nThanks for playing!")
            if __name__ == "__main__":
                sys.exit(f"\nBye {name}")
            else :
                return
    return play_guess_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="This program plays a game of guess the number with you."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player"
    )
    args = parser.parse_args()
    play = guess_number(args.name)
    play()
    