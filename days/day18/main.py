import turtle as t
from random import choice, randint
from hirst import rgb


tito = t.Turtle()
tito.speed('fast')
t.colormode(255)
colors = ['brown', 'navajo white', 'medium slate blue', 'lime green', 'purple']
#cores tiradas de https://trinket.io/docs/colors
angles = [0, 90, 180, 270]


def draw_square():
    for i in range(4):
        tito.right(90) #o valor é o angulo no qual ele virará
        tito.forward(50)
    

def dashed_lines():
    for i in range(0, 201, 10):
        tito.penup()
        tito.forward(5)
        tito.pendown()
        tito.forward(5)


def shapes():
    sides = 3
    while sides <= 10:
        angle = 360 / sides
        #tito.pencolor(choice(colors))
        tito.pencolor(random_colors())
        for n in range(sides):
            tito.right(angle)
            tito.forward(50)
        sides += 1

def random_walk():
    tito.pensize(3)
    for i in range(200):
        tito.pencolor(random_colors())
        tito.setheading(choice(angles))
        #tito.rt(choice(angles)) tinha sido minha escolha até ver a correção
        tito.forward(10)


def random_colors():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b


def circle(angle):    
    reps = int(360 / angle)
    for i in range(reps): 
        tito.pencolor(random_colors())
        tito.setheading(angle + tito.heading())
        tito.circle(80)
        
colors = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (167, 106, 56), (186, 159, 52), (6, 57, 83), 
(108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), 
(90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), 
(173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190), (37, 73, 84), 
(45, 74, 63), (48, 66, 80)]

def print_lines():
    pos_y = lines = 0
    step = 20
    while lines < 10:
        for i in range(10):
            tito.dot(10, choice(colors))
            tito.penup()
            tito.fd(step)
        pos_y += step
        tito.setpos(0, pos_y)
        lines += 1
print_lines()

screen = t.Screen()
screen.exitonclick()
