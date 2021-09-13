from turtle import Turtle, Screen
import random


def move(turtle):
    turtle.forward(random.randint(1, 10))


def race(tlist):
    while True:
        for i in tlist:
            move(i)
            if i.position()[0] >= 250:
                return i


screen = Screen()
screen.setup(width=520, height=500)
bid = screen.textinput("nim", "Enter your bid.")
tur = Turtle()
tim = Turtle()
ram = Turtle()
hari = Turtle()
tom = Turtle()
sanu = Turtle()
turtle_list = (tur, tim, ram, hari, tom, sanu)
color = ("blue", "red", "green", "yellow", "pink", "grey")
j = y = 0
for i in turtle_list:
    i.penup()
    i.speed("fastest")
    i.shape("turtle")
    i.color(color[j])
    j += 1
    y += 30
    i.setpos(-250, y)
winner = race(turtle_list)
print("The race has ended.\nThe winner is", winner.pencolor(), "turtle.")
if winner.pencolor() == bid:
    print("You won.")
else:
    print("You Loose.")
screen.exitonclick()
