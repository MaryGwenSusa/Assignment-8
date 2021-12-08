import random
import sys as broke
def header():
    title = "**LOTTERY**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def userBet():
    num = 1
    bets = []
    while num <= 3:
        try:
            guess = int(input(f"Enter guess #" + str(num) + "(0-9): ")) 
        except ValueError:
            print("You did not type an integer.")
            continue
        if (0 <= guess <= 9):
            if guess not in bets:
                bets.append(guess)
            else:
                print("Error! You have already picked this number")
                continue
        else:
            print("Invalid input: out of range.")
            continue
        num += 1
    return sorted(bets) 