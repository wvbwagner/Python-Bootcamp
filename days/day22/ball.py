from turtle import Turtle

class Ball(Turtle):

    UPPER_WALL = 280
    LOWER_WALL = -280

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 10
        self.y = 10


    def move_ball(self):
        set_x = self.xcor() + self.x
        set_y = self.ycor() + self.y
        self.setpos(set_x, set_y)


    def hit_wall(self):
        self.y = -(self.y)


    def hit_paddle(self):
        self.x = -(self.x)


    def reverse(self):
        self.home()
        self.x = -(self.x)