from turtle import Turtle, Screen
from random import randint
from time import sleep

INITIAL_POSX = -230

race = False

screen = Screen()
screen.setup(width=500, height=400)
ask = screen.textinput(title='Make a bet', prompt='Which turtle will win the race? Choose a color: ').strip().lower()

colors = ['red', 'green', 'blue', 'purple', 'brown', 'pink']
racers = []
size = len(colors)
posy = 90

for i in range(size):
    tito = Turtle('turtle')
    racers.append(tito)
    tito.penup()
    tito.speed('slow')
    tito.color(colors[i])
    tito.goto(INITIAL_POSX, posy)
    posy -= 30
    
if ask:
    race = True

winner = ''
while race:
    for racer in racers:
        if racer.pos()[0] >= 230.0:
            winner = racer.color()[0]
            race = False
            if ask == winner:
                print(f'You\'ve won, winner is {winner}!')
            else:
                print(f'You\'ve lost, winner is {winner}!')
        moves = randint(0, 10)
        racer.forward(moves)
