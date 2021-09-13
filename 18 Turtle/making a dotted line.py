from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()
tur.fillcolor("blue")
tur.shape("turtle")
tur.pencolor("red")
for _ in range(100):
    tur.forward(10)
    tur.penup()
    tur.forward(10)
    tur.pendown()

screen.screensize(12000, 800)
screen.exitonclick()
