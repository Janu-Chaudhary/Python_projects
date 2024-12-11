import random
import os

terminal_width = os.get_terminal_size().columns

header = "Ever wanted to feel like a psychic? Here’s your chance! Guess the secret number between 1 and 100"

print(header.center(terminal_width))

def easy_game():
    number=random.randint(1,50)
    for chance in range (1,4):
        print(f"Chance left: {3-chance}")
        guess_num=int(input("Guess the number:  "))
        if guess_num==number:
            if chance==1:
                print("")
            elif chance==2:
                print("")
            elif chance==3:
                print("")
           
        elif guess_num>number:
            print("")
        elif guess_num<number:
            print("")

def meadium_game():
    number=random.randint(1,100)
    for chance in range (1,4):
        print(f"Chance left: {3-chance}")
        guess_num=int(input("Guess the number:  "))
        if guess_num==number:
            if chance==1:
                print("")
            elif chance==2:
                print("")
            elif chance==3:
                print("")
        elif guess_num>number:
            print("")
        elif guess_num<number:
            print("")

def hard_game():
    number=random.randint(1,500)
    for chance in range (1,4):
        print(f"Chance left: {3-chance}")
        guess_num=int(input("Guess the number:  "))
        if guess_num==number:
            if chance==1:
                print("")
            elif chance==2:
                print("")
            elif chance==3:
                print("")
        elif guess_num>number:
            print("")
        elif guess_num<number:
            print("")
    
            


difficulty_level = int(input('''
        Do you want to play it safe, take a risk, or go all in? Your call:"
        [1] Easy: "Easy peasy, lemon squeezy. Numbers between 1 and 50!"
        [2] Medium: "Not too hot, not too cold—numbers between 1 and 100!"
        [3] Hard: "Go big or go home. Numbers between 1 and 500!"
        
        You have 3 chances to guess number in each level.
                             
        Enter the number of difficulity which you want to play: '''))
start=False
while start!=True:  
    try:
        if difficulty_level == 1:
            easy_game()
            start=True
        elif difficulty_level == 2:
            meadium_game()
            start=True
        elif difficulty_level == 3:
            hard_game()
            start=True
    except:
        print("Enter valid difficulty level")
        difficulty_level = int(input('''
        Do you want to play it safe, take a risk, or go all in? Your call:"
        [1] Easy: "Easy peasy, lemon squeezy. Numbers between 1 and 50!"
        [2] Medium: "Not too hot, not too cold—numbers between 1 and 100!"
        [3] Hard: "Go big or go home. Numbers between 1 and 500!"
        You have 3 chances to guess number in each level.
                         
        Enter the number of difficulity which you want to play: '''))



