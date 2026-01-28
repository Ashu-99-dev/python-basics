# Closure is a function having access to the scope of its parent function
# after the parent function has finished execution

def parent_function(person,coins):
    #coins = 3
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(f"{person} has {coins} coins left")
        elif coins == 1:
            print(f"{person} has {coins} coin left")
        else:
            print(f"{person} has no more coins left")
    return play_game

tommy = parent_function("tommy",3)
jerry = parent_function("jerry",5)
tommy()
tommy()
jerry()
jerry()
tommy() 
