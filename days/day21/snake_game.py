from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.tracer(0)

snake_play = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake_play.up)
screen.onkey(key='Left', fun=snake_play.left)
screen.onkey(key='Right', fun=snake_play.right)
screen.onkey(key='Down', fun=snake_play.down)  


play_on = True
while play_on:
    screen.update()
    sleep(0.1)
    snake_play.move_snake()
    #detect collision with food
    if snake_play.head.distance(food) < 15:
        food.food_position()
        snake_play.increase_snake()    
        scoreboard.add_score()
    #detect collision with wall or tail    
    if snake_play.hit_tail() or snake_play.hit_wall():
        play_on = False
        scoreboard.game_over()


screen.exitonclick()
