from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()
angle = 0


def forwards():
    tur.forward(15)


def backs():
    tur.back(15)


def ups():
    global angle
    angle += 5
    tur.setheading(angle)


def downs():
    global angle
    angle -= 5
    tur.setheading(angle)


def reset():
    tur.reset()
    tur.clear()


screen.listen()
screen.onkeypress(forwards, "d")
screen.onkeypress(backs, "a")
screen.onkeypress(ups, "w")
screen.onkeypress(downs, "s")
screen.onkeypress(reset, "r")
screen.screensize(1200, 800)
screen.exitonclick()
