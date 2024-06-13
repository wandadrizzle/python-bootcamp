#Section 4: Day 4 - Beginner - Randomisation and Python Lists


#Day 4 Project: Rock Paper Scissors, using https://ascii.co.uk/art
import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
    user_play = input()
    if user_play == "0":
        print(rock)
    elif user_play == "1":
        print(paper)
    elif user_play == "2":
        print(scissors)
    else:
        print("Invalid choice, game over!")
        restart = input("The game has ended would you like to play again? [yes/no] ")
        if restart.lower() == 'yes':
                print()
                continue
        else:
            print("Thanks for playing!")
            break

    computer_play = random.randint(0, 2)
    print("Computer played:")
    if computer_play == 0:
        print(rock)
    elif computer_play == 1:
        print(paper)
    else:
        print(scissors)

    if int(user_play) == computer_play:
        print("DRAW!")
    elif (int(user_play) == 0 and computer_play == 2) or (int(user_play) == 2 and computer_play == 1) or (int(user_play) == 1 and computer_play == 0):
        print("You Win!")
    elif (int(user_play) == 2 and computer_play == 0) or (int(user_play) == 1 and computer_play == 2) or (int(user_play) == 0 and computer_play == 1):
        print("You Lose!")

    restart = input("The game has ended would you like to play again? [yes/no] ")
    if restart.lower() == 'yes':
                print()
                continue
    else:
        print("Thanks for playing!")
        break
'''
https://www.askpython.com/
https://docs.python.org/3/
'''
exit()
import random, my_module

a = random.randint(1, 36)
print(a)
print(my_module.pi)

b = random.random() #A random float between zero and one
c = random.randint(0, 4) + random.random()
d = random.randrange(0, 5)
e = b * 5

print(b, c, d, e)

wanda = ["Words", "Worship", "Wisdom", "Workouts"]
print()
for thing in wanda:
    print(thing, end=" ")
print()
wanda[3] = "Wealth"
wanda.append("World")
wanda.append("Wonder")
wanda.extend(["Watch", "Waste", "Wear", "Walk", "Wait", "Will"])
print(wanda[-1])
print(f"Wanda can describe herself/interests interests in {len(wanda)} words.")

names_string = "Samkelo, Sandile, Sambulo, Sihle"
names = names_string.split(", ")
print(f"\n{names}")
payer = random.choice(names)
print(f"{payer} will cover the bill today.")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables] #A nested list
print()
print(dirty_dozen[1][1])
