from turtle import Turtle

ALIGN = 'center'
FONTS = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.add_score()


    def add_score(self):
        self.clear()
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONTS)
        self.score += 1


    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGN, font=FONTS)
