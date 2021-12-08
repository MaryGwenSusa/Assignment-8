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
