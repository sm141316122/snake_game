from turtle import Turtle
import os


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        if os.path.isfile("score_data.txt"):
            with open("score_data.txt") as f:
                self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))

    def add_score(self):
        self.score += 1
        self.refresh_score()

    def over(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("score_data.txt", "w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.refresh_score()
