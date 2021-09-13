import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.relocate()

    def relocate(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
