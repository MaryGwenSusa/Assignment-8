from random import randint as anyFT
def header():
    title = "**GUESS THE NUMBER**"
    flower = "*" * len(title) 
    print('\033[93m{} \n{} \n{}\033[00m'.format(flower, title, flower)) # created a header design
