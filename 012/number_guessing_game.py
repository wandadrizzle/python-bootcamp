#Global Constants

URL = "https://github.com/wandadrizzle/python-bootcamp"

#Final Project: The Number Guessing Game

import random, art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def guess(number, difficulty):

    if difficulty == "hard":
        attempts = HARD_ATTEMPTS
    elif difficulty == "easy":
        attempts = EASY_ATTEMPTS


    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1

        
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        elif guess == number:
            print(f"You got it! The answer was {number}.")
            break

        if attempts > 0 and guess != number:
            print("Guess again.\n")
        elif attempts == 0 and guess != number:
            print("You've run out of guesses, you lose.")

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and a 100\n")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1, 100)
#print(f"Pssst, the correct answer is {number}")
if difficulty == "easy" or difficulty == "hard":
    print()
    guess(number, difficulty)
else:
    print("You have selected an invalid option")
    exit()



