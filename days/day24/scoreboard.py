from turtle import Turtle

ALIGN = 'center'
FONTS = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt') as text:
            self.highscore = int(text.read())
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update_score()

    
    def update_score(self):
        self.clear()
        '''with open('highscore.txt') as text:
                self.highscore = int(text.read())'''
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGN, font=FONTS)


    def increase_score(self):
        self.score += 1
        self.update_score()


    def increase_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as text:
                text.write(str(self.highscore))


    def reset_score(self):
        self.score = 0
        self.update_score()
