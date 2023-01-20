from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setpos(-150, 200)
        self.write(f'Level {self.level}', align='center', font=('Arial', 20, 'normal'))

    def set_level(self):
        self.clear()
        self.level += 1
        self.setpos(-150, 200)
        self.write(f'Level {self.level}', align='center', font=('Arial', 20, 'normal'))
        return 0.1 * 0.8

    def game_over(self):
        self.setpos(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 20, 'normal'))
