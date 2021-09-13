import time
from snake import Snake
from turtle import Screen
from food import Food
from Score import Score
from collition import Collision

screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)
turtle_pos_list = [(0, 0), (-20, 0), (-40, 0)]
turtles = []

snake = Snake()
food = Food()
score = Score()
collision = Collision(snake)

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
score.score_board()

while collision.flag:
    screen.update()
    time.sleep(0.093)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.add_segment()
        score.score_board()
    collision.is_collied()
score.exit_screen()
screen.exitonclick()
