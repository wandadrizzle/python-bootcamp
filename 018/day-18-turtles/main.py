from turtle import Turtle, Screen, colormode
import heroes
from random import randint, choice
from my_colours import imibala

print(f"If I were a superhero I would be called {heroes.gen()}")

# https://docs.python.org/3/library/turtle.html#

franklin = Turtle()
print(franklin.shapesize())
# Output: (1.0, 1.0, 1)
franklin.shape('turtle')

# https://cs111.wellesley.edu/reference/colors, https://trinket.io/docs/colors
franklin.color('DarkOliveGreen')

screen = Screen()
# 1. SQUARE
count = 0
while count < 4:
    franklin.forward(100)
    franklin.right(90)
    count += 1

# 2. DASHED LINE
franklin.clear()
franklin.home()

# for _ in range(0, 15):
for _ in range(15):
    franklin.forward(10)
    franklin.penup()
    franklin.forward(10)
    franklin.pendown()

# 3. SHAPES: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
franklin.reset()

shapes = {
    "triangle": {"sides": 3},
    "square": {"sides": 4},
    "pentagon": {"sides": 5},
    "hexagon": {"sides": 6},
    "heptagon": {"sides": 7},
    "octagon": {"sides": 8},
    "nonagon": {"sides": 9},
    "decagon": {"sides": 10}
}

for shape in shapes:
    angle = 360 / shapes[shape]['sides']
    angle = round(angle, 2)
    # print(f"{shape} has {angle}° degrees")

    r = randint(0, 255) / 255.0
    g = randint(0, 255) / 255.0
    b = randint(0, 255) / 255.0

    franklin.color(r, g, b)

    count = 0
    while count < shapes[shape]['sides']:
        franklin.forward(100)
        franklin.right(angle)
        # franklin.forward(100)
        count += 1

# 4. Random walk
franklin.reset()

franklin.pensize(5)
franklin.forward(10)
franklin.shape('circle')
screen.bgcolor('black')
franklin.speed('fast')
franklin.shapesize(0.1, 0.1, 1)


def north(turtle: Turtle, distance: int):
    turtle.left(90)
    turtle.forward(distance)


def south(turtle: Turtle, distance: int):
    turtle.right(90)
    turtle.forward(distance)


def east(turtle: Turtle, distance: int):
    turtle.forward(distance)


def west(turtle: Turtle, distance: int):
    turtle.right(180)
    turtle.forward(distance)


movements = [north, south, east, west]
walk_amount = 10
begin_walk = 0
steps = 10

while begin_walk < walk_amount:
    turtle_colour = choice(imibala)
    franklin.color(turtle_colour)
    function = choice(movements)
    function(franklin, steps)
    begin_walk += 1

north(franklin, 10)


# My method above works but is a little long, knowing different ways to do something and wanting
# to practice what you've learnt is good BUT DON'T WASTE TIME!
# directions = [0, 90, 180, 270]
# franklin.setheading(choice(directions))

# https://www.w3schools.com/colors/colors_rgb.asp

colormode(255.0)


def random_color():

    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return red, green, blue


new_bg = random_color()
print(f"My new color is: {new_bg}.")
screen.bgcolor(new_bg)


# Challenge 5 - Spirograph

franklin.reset()
franklin.shape('arrow')
franklin.speed('fastest')
franklin.shapesize(0.1, 0.1, 1)

print(f"What can they tell me about my turtle: {franklin}.\nOh, so just that it's an object and I should "
      f"access the attributes individually. Cool, helpful.")

# for x in range(360):
for x in range(0, 360, 6):
    franklin.color(random_color())
    franklin.setheading(x)
    franklin.circle(100)

# screen.exitonclick()
screen.mainloop()
