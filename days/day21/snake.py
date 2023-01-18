from turtle import Turtle
from random import randint

DISTANCE =  20
POSITIONS =[(0,0),(-20,0),(-40,0)]
WALLS = (300.0, -300.0)

class Snake:

    def __init__(self) -> None:
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        
        for position in POSITIONS:
            tito = Turtle('square')
            tito.penup()
            tito.setpos(position)
            tito.color('white')
            self.segments.append(tito)

    
    def increase_snake(self):
        tuna = Turtle('square')
        tuna.penup()
        tuna.setpos(self.segments[-1].pos())
        tuna.color('white')
        self.segments.append(tuna)
        

    def move_snake(self):
        for snk_pos in range(len(self.segments) -1, 0, -1): #move snake[2] para a posição de snake[1] e snake[1] para snake[0]
            new_pos = self.segments[snk_pos - 1].pos() #pega a posição de snake[1]
            self.segments[snk_pos].setpos(new_pos) #coloca a posição de snake 1 em snake 2
        self.segments[0].forward(DISTANCE)


    def hit_wall(self):
        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            return True
        return False

    def hit_tail(self):
        for segments in self.segments[1:]:
            if self.head.distance(segments) <= 10:
                return True
        return False


    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)


    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)


    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

