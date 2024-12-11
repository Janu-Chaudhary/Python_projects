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
            if chance == 1:
                print(f"Wow! You guessed it on your first try! The number was {number}. You're a genius!")
            elif chance == 2:
                print(f"Great job! You got it on your second try! The number was {number}. Well done!")
            elif chance == 3:
                print(f"Nice work! You figured it out on your third try! The number was {number}. Persistence pays off!")
            return
        elif guess_num > number:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a larger number.")
    print(f"Sorry, you've run out of chances! The correct number was {number}.")
def meadium_game():
    number=random.randint(1,100)
    for chance in range (1,4):
        print(f"Chance left: {3-chance}")
        guess_num=int(input("Guess the number:  "))
        if guess_num == number:
            if chance == 1:
                print(f"Fantastic! You nailed it on your first attempt! The number was {number}. You're amazing!")
            elif chance == 2:
                print(f"Awesome! You guessed it on your second try! The number was {number}. Great job!")
            elif chance == 3:
                print(f"Well done! You got it on your third attempt! The number was {number}. Keep it up!")
            return
        elif guess_num > number:
            print("Oops! That's too high. Give it another shot.")
        else:
            print("Not quite! That's too low. Try again.")
    print(f"Game over! The secret number was {number}.")

def hard_game():
    number=random.randint(1,500)
    for chance in range (1,4):
        print(f"Chance left: {3-chance}")
        guess_num=int(input("Guess the number:  "))
        if guess_num==number:
            if chance == 1:
                print(f"Incredible! You guessed it right on your first try! The number was {number}. You're a legend!")
            elif chance == 2:
                print(f"Awesome job! You got it on your second attempt! The number was {number}. Well played!")
            elif chance == 3:
                print(f"You did it! It took you three tries, but you got there! The number was {number}. Nice effort!")
            return
        elif guess_num > number:
            print("That's a bit too high. Lower your sights!")
        else:
            print("That's a bit too low. Aim higher!")
    print(f"Alas, you've used all your chances! The correct answer was {number}.")
    
            


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



