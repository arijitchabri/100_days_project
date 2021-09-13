# import colorgram
# colors = colorgram.extract("download.jpg", 10)
# color_list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tur = Turtle()
screen = Screen()
screen.screensize(1200, 1200)
tur.pensize(20)
tur.speed("fast")
tur.penup()
tur.hideturtle()
color_list = [(203, 160, 121), (241, 216, 82), (210, 74, 138), (97, 189, 209), (174, 56, 113), (213, 127, 169)]
tur.pensize(20)
x = -270
y = -200
tur.setpos(x, y)
for i in range(10):
    for j in range(10):
        tur.dot(20, random.choice(color_list))
        tur.forward(50)
    y += 50
    tur.setpos(x, y)

screen.exitonclick()
