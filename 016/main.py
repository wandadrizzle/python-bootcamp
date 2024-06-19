# Object Oriented Programming

import class_example as c
import turtle
import prettytable

# https://docs.python.org/3/library/turtle.html

car = c.Car("Audi ", "Q8 e-tron", 2024)
# This is how you get the attribute
print(car.model)

print()
franklin = turtle.Turtle()
print(franklin)
franklin.shape("turtle")
# https://cs111.wellesley.edu/reference/colors
franklin.color('DarkOliveGreen')
my_screen = turtle.Screen()
franklin.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()


# https://pypi.org/, https://pokemondb.net/pokedex/game/x-y,
# https://pypi.org/project/prettytable/, https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

print()

table = prettytable.PrettyTable()

# This didn't quiet work
table.align = "l"

print(table.align)
table.add_column("Name", ["John", "Sam", "Tom"])
table.add_column("Surname", ["Doe", "Witwicky", "Hanks"])
table.align["Name"] = 'l'
table.align["Surname"] = 'l'
print(table)
