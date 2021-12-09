from random import randint as anyFT
def header():
    title = "**GUESS THE NUMBER**"
    flower = "*" * len(title) 
    print('\033[93m{} \n{} \n{}\033[00m'.format(flower, title, flower)) # created a header design

def guessingNumber():
    UserName = input("\033[36mHello, what's your name?\033[00m \033[91m^_^\n>>>\033[00m ").title()
    print('\033[92mOkay, '+ UserName + '. You are guessing a number between \033[1m0 and 100.\033[00m')
    secretNum = anyFT(0,100) #random.choice
    numberOfGuesses = True
    while numberOfGuesses:
        try:
            guess = int(input("\033[95mWhat's your guess?\033[00m\n\033[93m>>>\033[00m "))
        except ValueError: # input validation for decimals and alpa format
            print("\033[33mYou did not type an \033[4minteger.\033[00m")
            continue