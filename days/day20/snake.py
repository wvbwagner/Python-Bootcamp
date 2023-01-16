from turtle import Turtle
from random import randint

DISTANCE =  20


class Snake:

    def __init__(self) -> None:
        
        self.segments = []
        self.position = 0
        self.create_snake()
        

    def create_snake(self):
        
        for i in range(3):
            tito = Turtle('square')
            tito.penup()
            tito.setx(self.position)
            tito.color('white')
            self.segments.append(tito)
            self.position -=20

    def move_snake(self):
        
        for snk_pos in range(len(self.segments) -1, 0, -1): #move snake[2] para a posição de snake[1] e snake[1] para snake[0]
            new_pos = self.segments[snk_pos - 1].pos() #pega a posição de snake[1]
            self.segments[snk_pos].setpos(new_pos) #coloca a posição de snake 1 em snake 2
        self.segments[0].forward(DISTANCE)   


    def up(self):
        if self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() != 90.0:
            self.segments[0].setheading(270)
