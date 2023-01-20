from turtle import Screen, Turtle
from cars import Cars
from player import Player
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.move_player)



play_on = True
time = 0.1
while play_on:
    sleep(time)
    screen.update()
    cars.create_cars()
    cars.move_car()
    if player.ycor() > 280:
        scoreboard.set_level()
        player.repositioning_player()
        time *= 0.8
    for car in cars.cars:
        if car.distance(player) <= 20:
            play_on = False
            scoreboard.game_over()
    

screen.exitonclick()