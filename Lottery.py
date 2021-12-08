import random
import sys as broke
def header():
    title = "**LOTTERY**"
    print("*" * len(title)) # created a header design
    print(title)
    print("*" * len(title))

def userBet():
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
    return sorted(bets)

def winningNumbers():
    lotteryNumbers = list() # variable for a list function
    winningNum = sorted(random.sample(range(0,9), 3)) 
    lotteryNumbers.append(winningNum) # adds items on the lotteryNumbers variable (for list)
    return lotteryNumbers

def evaluator(userBet, lottoNum):
    print("Your bet were:", userBet)
    print("The winning numbers are:", lottoNum)
    if userBet == lottoNum:
        print ("\033[32m\033[1mWinner!^__^\033[00m")
    else:
        print ("\033[34mYou lose :<\033[00m")

def main():
    tryAgain = True
    while tryAgain:
        betNumbers = userBet()
        lottoResult = winningNumbers()
        evaluator(betNumbers, lottoResult)

confirm = 'y'
while 'y' in confirm:
    chance = input("\033[35mTry Again? \033[3mY/N\033[00m \n>>> ").lower()
    if "y" in chance:
        print("\033[36mThis might be your lucky round! ^__^\033[00m")
        main()