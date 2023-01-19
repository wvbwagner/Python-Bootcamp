from turtle import Turtle

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

class Paddle(Turtle):

    def __init__(self, positions) -> None:
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.setpos(positions)

    def up(self):
        if self.ycor() < 240:
            sety = self.ycor() + 20
            self.setpos(self.xcor(), sety)        

    
    def down(self):
        if self.ycor() > -240:
            sety = self.ycor() - 20
            self.setpos(self.xcor(), sety)

    def draw_line(self):
        tuna = Turtle()
        tuna.hideturtle()
        tuna.color('white')
        tuna.penup()
        tuna.setpos(0, 300)
        tuna.right(90)
        for i in range(300):
            tuna.pendown()
            tuna.fd(20)
            tuna.penup()
            tuna.fd(20)