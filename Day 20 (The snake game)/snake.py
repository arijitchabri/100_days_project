from turtle import Turtle

move_distance = 10


class Snake:
    def __init__(self):
        self.turtles = []
        self.turtle_pos_list = [(0, 0), (-20, 0), (-40, 0)]

        for i in self.turtle_pos_list:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.setpos(i)
            self.turtles.append(new_turtle)
            self.head = self.turtles[0]

    def move_snake(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def add_segment(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.setpos(self.turtles[len(self.turtles)-1].position())
        self.turtles.append(new_turtle)
        self.head = self.turtles[0]
