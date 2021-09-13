import random
import turtle
from turtle import Turtle, Screen


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_return = (r, g, b)
    return color_return


tur = Turtle()
turtle.colormode(255)
angles = [0, 90, 180, 270]
screen = Screen()
angle = 0
tur.pensize(10)
tur.speed("fastest")
for i in range(1, 300):
    tur.forward(30)
    tur.setheading(random.choice(angles))
    tur.pencolor(color())

screen.screensize(12000, 8000)
screen.exitonclick()
