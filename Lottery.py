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
        resultLoop()

def resultLoop():
    confirm = 'y'
    while 'y' in confirm:
        chance = input("\033[35mTry Again? \033[3mY/N\033[00m \n>>> ").lower()
        if "y" in chance:
            print("\033[36mThis might be your lucky round! ^__^\033[00m")
            main()
        elif "n" in chance:
            print("\033[32mThank you for playing! <<3\033[00m")
            broke.exit()
        elif not("y" in chance) and not("n" in chance):
            print("\033[31m\033[1mInvalid input:\033[00m \033[35mnone of the choices.\033[00m")
            continue

header()
main()


# another version with different functions and displays result like a table; one calling point
import random
import sys as broke
def userBet():
    num = 1
    bets = []
    while num <= 3:
        try:
            guess = int(input(f"\033[00mEnter guess #" + str(num) + "(0-9):\033[93m ")) 
        except ValueError:
            print("\033[00m033[33mYou did not type an \033[4minteger.\033[00m")
            continue
        if (0 <= guess <= 9):
            if guess not in bets:
                bets.append(guess)
            else:
                print("\033[00m\033[31m\033[1mError!\033[00m \033[34mYou have \033[4malready picked this number\033[00m")
                continue
        else:
            print("\033[00m\033[31m\033[1mInvalid input:\033[00m \033[35mout of range.\033[00m")
            continue
        num += 1
    return sorted(bets)

def winningNumbers():
    lotteryNumbers = []
    for numsEntry in range(3):
        winningNum = random.randint(0,9)
        while winningNum in lotteryNumbers: # if duplicate, generate new integer
            winningNum = random.randint(0,9)
        lotteryNumbers.append(winningNum)
    return sorted(lotteryNumbers)
# would also work with the use of list(range()) and random.choice; or same structure with randrange()
    
def evaluator(userBet, lottoNum):
    lines = (f"{'----':>5}     {'---------------':>5}")
    print(f"\033[00m\033[46m{'Bets':>5}\033[00m     \033[42m{'Winning Numbers':>5}\033[00m \n{lines}")
    for uB, lN in zip(userBet, lottoNum): # connotates that the variables are lists
        print(f"\033[31m{uB:>4.0f}     {lN:>9.0f}\033[00m")
    print(lines)
    if userBet == lottoNum:
        print ("\033[32m\033[1mWinner!^__^\033[00m")
    else:
        print ("\033[34mYou lose :<\033[00m")

def main():
    title = "**LOTTERY**"
    flower = "*" * len(title) 
    print('\033[93m{} \n{} \n{}\033[00m'.format(flower, title, flower)) # created a header design
    tryAgain = True
    while tryAgain:
        betNumbers = userBet()
        lottoResult = winningNumbers()
        evaluator(betNumbers, lottoResult)
        resultLoop()

def resultLoop():
    confirm = 'y'
    while 'y' in confirm:
        chance = input("\033[35mTry Again? \033[3mY/N\033[00m \n>>> ").lower()
        if "y" in chance:
            print("\033[36mThis might be your lucky round! ^__^\033[00m")
            main()
        elif "n" in chance:
            print("\033[32mThank you for playing! <<3\033[00m")
            broke.exit()
        if not("y" in chance) and not("n" in chance):
            print("\033[31m\033[1mInvalid input:\033[00m \033[35mnone of the choices.\033[00m")
            continue

main()