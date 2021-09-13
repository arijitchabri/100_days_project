from turtle import Turtle, Screen

tur = Turtle()
tim = Turtle
ari = tim()

screen = Screen()
tur.fillcolor("blue")
tur.shape("turtle")
tur.pencolor("red")

for _ in range(4):
    tur.forward(100)
    tur.right(90)
tur.setpos(100, 100)
screen.screensize(1200, 800)
screen.exitonclick()
