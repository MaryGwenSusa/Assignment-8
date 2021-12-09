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
        no = "\033[31m\033[1mInvalid input:\033[00m \033[35mout of range.\033[00m"
        if guess > secretNum:
            if not(guess > 100):
                print("\033[31mYour guess is \033[4mgreater than\033[0m \033[31mthe \033[3mrandom number!\033[00m")
            else:
                print(no)
        elif guess < secretNum:
            if not(guess < 0):
                print("\033[32mYour guess is \033[4mless than\033[0m \033[32mthe \033[3mrandom number!\033[00m")
            else:
                print(no)
        else:
            print("\033[34mYou have guessed it right! Good job, %s ^__^\033[00m" % (UserName))
            break

header()
guessingNumber()