from turtle import Turtle
from random import choice, randint

COLORS = ['green', 'blue', 'yellow', 'orange', 'pink', 'purple', 'brown', 'red']


class Cars:

    def __init__(self) -> None:
       
        self.cars = []

    def create_cars(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape('square')
            car.penup()
            car.turtlesize(stretch_len=2)
            car.setpos(300, randint(-250, 250))
            car.color(choice(COLORS))
            self.cars.append(car)
    

    def move_car(self):
        for car in self.cars:
            getx = car.xcor() - 5
            car.setx(getx)


        



