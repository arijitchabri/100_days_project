from turtle import Turtle

Alignment = "center"
Font = ("Courier", 15, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.txt = open("score.txt")
        self.high_score = int(self.txt.readline())
        self.give_score = -1
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.color("white")

    def score_board(self):
        self.clear()
        self.give_score += 1
        msg = "Score : " + str(self.give_score)
        self.write(msg, False, Alignment, Font)

    def exit_screen(self):
        self.setpos(0, 0)
        msg = f"Game Over the High score is {self.high_score}"
        if self.give_score > self.high_score:
            msg = f"You made a highscore of {self.give_score}"
            self.txt = open("score.txt", "w")
            self.txt.write(str(self.give_score))

        self.write(msg, False, Alignment, Font)


score = Score()
