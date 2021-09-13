import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from player import Player


scr = Screen()
scr.bgcolor("Black")
scr.tracer(0)
scr.setup(800, 600)
paddle1 = Paddle()
paddle2 = Paddle()
paddle1.set_to_right()
paddle2.set_to_left()
ball = Ball()
scr.listen()
scr.onkeypress(paddle1.move_up, "w")
scr.onkeypress(paddle1.move_down, "s")
scr.onkeypress(paddle2.move_up, "Up")
scr.onkeypress(paddle2.move_down, "Down")
ball.reset_the_ball_right()
turtle.title("Pong Game")
p1 = Player((-100, 250), "Arijit")
p2 = Player((100, 250), "Suman")

while True:
    time.sleep(0.005)
    ball.frwd()
    if ball.ball.ycor() < -290 or ball.ball.ycor() > 290:
        ball.bounce_y()
    if ball.ball.xcor() < -400:
        p1.score_counter()
        ball.reset_the_ball_right()
    if ball.ball.xcor() > 400:
        p2.score_counter()
        ball.reset_the_ball_left()
    if (ball.ball.xcor() > -350 and ball.ball.distance(paddle2.paddle.xcor(), paddle2.paddle.ycor()) <= 15) \
            or (ball.ball.xcor() < 350 and ball.ball.distance(paddle1.paddle.xcor(), paddle1.paddle.ycor()) <= 15):
        ball.bounce_x()
    scr.update()
