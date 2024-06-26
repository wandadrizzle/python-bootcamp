# The Snake Game - started 25 June 2024, tried completing this on the 26th

from turtle import Screen, Turtle
import time

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
    head_body.setposition((placement * - 20), 0)
    snake.append(head_body)

# 2. Movement
# def move_forward():
def go_right():

    if snake[0].heading() == 0:
        isnake_length = len(snake) - 1
        for part in range(isnake_length, 0, -1):
            portion = snake[part]
            x_next, y_next = snake[part - 1].position()
            portion.setposition(x_next, y_next)
        x, y = snake[0].position()
        snake[0].setposition(x + 20, y)
    elif snake[0].heading() == 90:
        snake[0].setheading(0)
        go_right()
    elif snake[0].heading() == 180: # can't go right when facing left
        pass
    elif snake[0].heading() == 270:
        snake[0].setheading(0)
        go_right()



def go_left():

    if snake[0].heading() == 0: # can't go left when facing right
        pass
    elif snake[0].heading() == 90:
        snake[0].setheading(180)
        go_left()
    elif snake[0].heading() == 180:
        isnake_length = len(snake) - 1
        for part in range(isnake_length, 0, -1):
            portion = snake[part]
            x_next, y_next = snake[part - 1].position()
            portion.setposition(x_next, y_next)
        x, y = snake[0].position()
        snake[0].setposition(x - 20, y) 
    elif snake[0].heading() == 270:
        snake[0].setheading(90)
        go_left()
               
    

def go_down():

    if snake[0].heading() == 0:
        snake[0].setheading(270)
        go_down()
    elif snake[0].heading() == 90: # can't go down when facing up
        pass
    elif snake[0].heading() == 180:
        snake[0].setheading(270)
        go_down()
    elif snake[0].heading() == 270:
        isnake_length = len(snake) - 1
        for part in range(isnake_length, 0, -1):
            portion = snake[part]
            x_next, y_next = snake[part - 1].position()
            portion.setposition(x_next, y_next)
        x, y = snake[0].position()
        snake[0].setposition(x, y - 20)  


def go_up():

    if snake[0].heading() == 0:
        snake[0].setheading(90)
        go_up()
    elif snake[0].heading() == 90:
        isnake_length = len(snake) - 1
        for part in range(isnake_length, 0, -1):
            portion = snake[part]
            x_next, y_next = snake[part - 1].position()
            portion.setposition(x_next, y_next)
        x, y = snake[0].position()
        snake[0].setposition(x, y + 20)
    elif snake[0].heading() == 180:
        snake[0].setheading(90)
        go_up()
    elif snake[0].heading() == 270: # can't go up when facing down
        pass  


screen.listen()
# screen.onkeypress(move_forward, "r")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# 3. Control

# 4. Detect food collision

# 5. Create a scoreboard

# 6. Detect wall collision

# 7. Detect collision with tail


screen.exitonclick()

notes = r"""
Angela spoke about a tracer, screen update and delay
"""
