from turtle import Turtle


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.repositioning_player()
        self.setheading(90)


    def move_player(self):
        if self.ycor() < 290:
            x = self.ycor() + 10
            self.sety(x)

    def repositioning_player(self):
        self.setpos(0, -280)
