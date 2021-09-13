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
screen = Screen()
tur.speed("fastest")
angle = 0
for _ in range(60):
    tur.circle(100)
    tur.setheading(angle)
    angle += 6
    tur.color(color())

screen.screensize(12000, 8000)
screen.exitonclick()