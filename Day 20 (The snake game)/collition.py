class Collision:
    def __init__(self, snake):
        self.snake = snake
        self.flag = True

    def is_collied(self):
        if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290:
            self.flag = False
        elif self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290:
            self.flag = False
        self.tail_bite()

    def tail_bite(self):
        head = self.snake.head
        for i in range(1, len(self.snake.turtles)):
            if head.distance(self.snake.turtles[i]) < 1:
                self.flag = False
