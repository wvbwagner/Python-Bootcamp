from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(position)
        self.color('white')
        self.write(f'{self.score}', align='center', font=('Arial', 24, 'normal'))


    def add_scoreboard(self):
        self.clear()
        self.color('white')
        self.score += 1
        self.write(f'{self.score}', align='center', font=('Arial', 24, 'normal'))
        return self.score
        

