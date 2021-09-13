import random
from turtle import Turtle

col_lst = ["red", "green", "blue", "yellow", "brown"]

class Block:
    def __init__(self):
        self.block = Turtle()
        self.block.penup()
        self.block.shapesize(stretch_wid=1, stretch_len=2)
        self.block.setheading(180)
        self.block.goto(random.randint(150, 300), random.randint(-260, 260))
        self.block.color(random.choice(col_lst))
        self.block.shape("square")
        self.block.speed("slowest")
        self.move()

    def move(self):
        if self.block.xcor() < -300:
            self.block.goto(random.randint(150, 300), random.randint(-260, 260))
        else:
            self.block.forward(10)

