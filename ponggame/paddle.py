from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shapesize(stretch_wid=3, stretch_len=1)
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("White")
    def set_to_right(self):
        self.paddle.setpos(-380, 0)

    def set_to_left(self):
        self.paddle.setpos(380, 0)

    def move_up(self):
        if self.paddle.ycor() < 300:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+20)

    def move_down(self):
        if self.paddle.ycor() > -280:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-20)