import sys
from turtle import Turtle, Screen
Alignment = "center"
Font = ("Courier", 15, "bold")
sc = Screen()


class Player(Turtle):
    def __init__(self, cor, name=None):
        super().__init__()
        self.name = name
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(cor)
        self.msg = name
        self.color("White")
        self.write(self.msg + " " + str(self.score), False, Alignment, Font)

    def score_counter(self):
        self.score += 1
        self.clear()
        self.write(self.msg+str(self.score), False, Alignment, Font)
        if self.score > 4:
            self.goto(0, 0)
            self.msg = "Hurrah!!!! " + self.name + ", has won the game."
            self.write(self.msg, False, Alignment, Font)
            sc.exitonclick()
            sys.exit()
