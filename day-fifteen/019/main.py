# Event Listeners

from turtle import Turtle, Screen
from random import randint

franklin = Turtle('turtle')
screen = Screen()

def move_forward():
    franklin.forward(10)

# Using a function as an input, you don't need the brackets when pushing the function as an argument.
# The parenthesis trigger the method to happen there and then
screen.listen()
# screen.onkey(key="space", fun=move_forward)

def backwards():
    franklin.backward(10)


def counter_clockwise():
    franklin.left(10)
    # franklin.setheading(franklin.heading + 10)


def clockwise():
    franklin.right(10)


def clear_drawing():
    franklin.reset()
    screen.resetscreen()


# Note: onkey accepts a function with no arguments

etch_a_sketch = r"""
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
"""

screen.clear()
# Instances of objects with different states

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(f"The user guessed that {user_bet} will be the winner.")
racers = []

for color_index in range(len(rainbow)):
    tortoise = Turtle(shape="turtle")
    tortoise.penup()
    tortoise.color(rainbow[color_index])
    tortoise.goto(x=-240, y=-70 + 30 * color_index)
    racers.append(tortoise)

# print(racers)
if user_bet:
    race_on = True
    while race_on:
        for turtle in racers:
            x, y = turtle.position()
            # print(turtle.position())
            # print(turtle.color())
            if x >= 230:
                print(f"{turtle.color()[0].title()} won!", end=" ")

                if turtle.color()[0] == user_bet:
                    print(f"You win!")
                else:
                    print(f"You lose!")
                
                race_on = False
                break
            steps =  randint(1, 10)
            turtle.forward(steps)

screen.mainloop()

