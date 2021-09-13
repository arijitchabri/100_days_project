import time
from turtle import Turtle, Screen
from Moving_obj import Block


def move_up():
    tur.forward(20)


def back():
    tur.back(20)


Alignment = "center"
Font = ("Courier", 15, "bold")
scr = Screen()
tur = Turtle()
sco = Turtle()
msg = "Level "
score = 0

scr.setup(width=600, height=600)
scr.tracer(0)
scr.bgcolor("White")
tur.shape("turtle")
tur.penup()
tur.goto(0, -280)
tur.setheading(90)
scr.title("Dodge the cars")
scr.listen()
scr.onkeypress(move_up, "Up")
scr.onkeypress(back, "Down")
sco.penup()
sco.hideturtle()
sco.goto(-250, 260)
sco.write(msg+"0", False, Alignment, Font)
flag = True
count = 0
lst = []


while flag:
    if count < 15:
        for i in range(2):
            i = "i"+str(i)
            i = Block()
            lst.append(i)
            count += 1
    scr.update()
    time.sleep(.08)
    for i in lst:
        i.move()
        if i.block.distance(tur.xcor(), tur.ycor()) < 10:
            flag = False
            sco.clear()
            sco.goto(0, 0)
            sco.write(" !! Hey You Loose !! ", False, Alignment, Font)
    if tur.ycor()>290:
        tur.goto(0, -280)
        score += 1
        sco.clear()
        sco.write(msg+str(score), False, Alignment, Font)

        if score > 5:
            sco.goto(0, 0)
            sco.write(" !! Hey You Win !! ", False, Alignment, Font)
            flag = False

    if tur.ycor() < -300:
        tur.goto(0, -280)


scr.exitonclick()
