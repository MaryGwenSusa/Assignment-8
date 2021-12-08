import random
import sys as broke
def header():
    title = "**LOTTERY**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))


num = 1
bets = [] # initialized an empty list
while num <= 3: # limit for the input loop
    try:
        guess = int(input(f"Enter guess #" + str(num) + "(0-9): ")) 
    except ValueError: # input validation for decimals and alpa format
        print("\033[33mYou did not type an \033[4minteger.\033[00m")
        continue
    if (0 <= guess <= 9):
        if guess not in bets: # no duplicates
            bets.append(guess)
        else:
            print("\033[31m\033[1mError!\033[00m \033[34mYou have \033[4malready picked this number\033[00m")
            continue
    else:
        print("\033[31m\033[1mInvalid input:\033[00m \033[35mout of range.\033[00m")
        continue
    num += 1