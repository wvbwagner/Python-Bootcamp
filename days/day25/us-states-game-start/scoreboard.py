from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
