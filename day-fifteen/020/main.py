# The Snake Game - started 25 June 2024

from turtle import Screen, Turtle

screen = Screen()
screen.title("Wanda's Snake Game")
screen.setup(600, 600)
screen.bgcolor('black')

# 1. Body
snake = []

for placement in range(3):
    head_body = Turtle('square')
    head_body.color('white')
    # print(head_body.shapesize())
    head_body.penup()
    head_body.setposition((placement * 20), 0)
    snake.append(head_body)

# 2. Movement
def move_forward():
    for part in range(len(snake)):
        portion = snake[part]
        portion.penup()
        x, y = portion.position()
        portion.setposition(x + 20, y)

screen.listen()
screen.onkeypress(move_forward, "r")

# 3. Control

# 4. Detect food collision

# 5. Create a scoreboard

# 6. Detect wall collision

# 7. Detect collision with tail


screen.exitonclick()