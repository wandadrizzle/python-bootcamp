# Challenge 6 - MILLION DOLLAR PAINTING, The Hirst Painting Project
import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

hirst_colours = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241),
                 (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                 (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
                 (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
                 (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                 (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
                 (107, 127, 153), (176, 192, 208), (168, 99, 102)]

arbie = turtle.Turtle()
arbie.shape('arrow')
arbie.shapesize(0.05, 0.05, 1)

screen = turtle.Screen()
turtle.colormode(255.0)

arbie.speed('normal')
x, y = arbie.position()
print("Turtle's position at the beginning", arbie.position())

screen.setworldcoordinates(-100, -100, 600, 600)

for y_value in range(11):
    if y_value == 10:
        random_color = random.choice(hirst_colours)
        arbie.dot(20, random_color)
        arbie.penup()
        arbie.setposition(0, y_value * 50)
        arbie.hideturtle()
        break
    for x_value in range(10):
        random_color = random.choice(hirst_colours)
        arbie.dot(20, random_color)
        arbie.teleport(50 * x_value, y_value * 50)

        # print("Turtle's current position", arbie.position())

print("\nTurtle's position at the end", arbie.position())


screen.mainloop()

# [Rgb(r=245, g=243, b=238), Rgb(r=246, g=242, b=244), Rgb(r=202, g=164, b=110),
# Rgb(r=240, g=245, b=241), Rgb(r=236, g=239, b=243), Rgb(r=149, g=75, b=50),
# Rgb(r=222, g=201, b=136), Rgb(r=53, g=93, b=123), Rgb(r=170, g=154, b=41),
# Rgb(r=138, g=31, b=20), Rgb(r=134, g=163, b=184), Rgb(r=197, g=92, b=73),
# Rgb(r=47, g=121, b=86), Rgb(r=73, g=43, b=35), Rgb(r=145, g=178, b=149),
# Rgb(r=14, g=98, b=70), Rgb(r=232, g=176, b=165), Rgb(r=160, g=142, b=158),
# Rgb(r=54, g=45, b=50), Rgb(r=101, g=75, b=77), Rgb(r=183, g=205, b=171),
# Rgb(r=36, g=60, b=74), Rgb(r=19, g=86, b=89), Rgb(r=82, g=148, b=129),
# Rgb(r=147, g=17, b=19), Rgb(r=27, g=68, b=102), Rgb(r=12, g=70, b=64),
# Rgb(r=107, g=127, b=153), Rgb(r=176, g=192, b=208), Rgb(r=168, g=99, b=102)]


# https://chocolatey.org/install#individual - this didn't work
# pillow-10.3.0-cp311-cp311-win_amd64.whl from https://www.wheelodex.org/projects/pillow/
# pip install "LOCATION OF DOWNLOAD" --force-reinstall

#  ERROR: Failed building wheel for Pillow
# ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (Pillow)

# PS C:\Windows\system32> pip --version
# pip 24.1 from C:\Python311\Lib\site-packages\pip (python 3.11)

# What's going on? https://sourceforge.net/projects/zlib/, [THIS ONE!!] https://zlib.net/

notes = r'''
1. I downloaded the permalink
2. Extracted the zip
3. Opened the cmd [Press Win + R, type cmd, and press Enter.]
4. cd path-to-extracted-directory
5. .\configure
6. nmake -f win32\Makefile.msc

---DEAD END

Okay, so turns out I need to install CMAKE then do what they say I should do here:
https://github.com/horta/zlib.install
This might also be helpful: https://eclipsebook.in/appendix/setting-up-zlib/
This came up from time to time: http://www.libpng.org/pub/png/libpng.html

15:38 ANGISAZI KE MANJE 
- https://pillow.readthedocs.io/en/latest/installation/building-from-source.html#building-from-source
'''
