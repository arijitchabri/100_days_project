import random
from turtle import Turtle, Screen

tur = Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "violet", "pink", "brown"]
screen = Screen()
angle = 0
sides = 0
for i in range(3, 11):
    for j in range(i):
        tur.forward(100)
        tur.right(360 / i)
    tur.pencolor(random.choice(colors))
screen.screensize(1200, 800)
screen.exitonclick()
