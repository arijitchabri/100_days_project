import random
from turtle import Turtle

heading = 0


class Ball:
    def __init__(self):
        self.ball = Turtle()
        b = self.ball
        b.shape("square")
        b.shapesize(.7)
        self.ball.penup()
        self.ball.color("White")
        self.ball.shape("circle")
        self.ballx = 1
        self.bally = 1

    def frwd(self):
        x = self.ball.xcor()+self.ballx
        y = self.ball.ycor()+self.bally
        self.ball.goto(x, y)

    def reset_the_ball_right(self):
        global heading
        self.ball.setpos(0, random.randint(-150, 150))
        self.ball.setheading(heading)

    def reset_the_ball_left(self):
        global heading
        self.ball.setpos(0, random.randint(-150, 150))
        self.ball.setheading(heading)

    def bounce_y(self):
        self.bally *= -1

    def bounce_x(self):
        self.ballx *= -1


