from turtle import Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()

snake_play = Snake()


screen.onkey(key='Up', fun=snake_play.up)
screen.onkey(key='Left', fun=snake_play.left)
screen.onkey(key='Right', fun=snake_play.right)
screen.onkey(key='Down', fun=snake_play.down)  


play_on = True
while play_on:
    screen.update()
    sleep(0.3)
    snake_play.move_snake()
      

        

screen.exitonclick()

