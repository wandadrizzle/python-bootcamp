#Section 3: Day 2 - Beginner - Control Flow and Logical Operators
#Use a multiblock sting - https://ascii.co.uk/art, creativity is on zero
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


choice_one = input("left or right? ")
choice_one = choice_one.capitalize()

if choice_one == "Left":
    choice_two = input("Swim or Wait ")
    choice_two = choice_two.capitalize()
  
    if choice_two == "Wait":
        choice_three = input("Which door? [Blue, Red or Yellow?] ")
        choice_three = choice_three.capitalize()
        if choice_three == "Blue" or choice_three == "Red":
            if choice_three == "Blue":
                print("You were eated by beasts 👹")
            else:
                print("You were burned by fire. 🔥")
            print("Game Over. 💀")
        elif choice_three == "Yellow":
            print("You Win! 🏆🏴‍☠️")
        else:
            print("You selected an invalid input, game over! 💀")
    elif choice_two == "Swim":
        print("You were attacked by trout 🦈. Game Over. 💀")
    else:
        print("You selected an invalid input, game over! 💀")
elif choice_one == "Right":
    print("You fell into a hole 🕳️. Game Over. 💀")
else:
    print("You selected an invalid input, game over! 💀")

exit()
age = 15
bill = 0

if age > 18:
    print('Adult tickets are $10.')
    bill += 10
elif age < 12:
    print('Child tickets are $5.')
    bill += 5
else:
    print('Youth tickets are $7.')
    bill += 7

print(f"Your bill is ${bill}.")

#and, not, or
