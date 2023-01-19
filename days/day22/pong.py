from turtle import Screen
from time import sleep
from move_paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

R_SCORE_POS = (50, 260)
L_SCORE_POS = (-50, 260)

screen = Screen()

screen.setup(width=800, height= 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_paddle.draw_line()
ball = Ball()
r_scoreboard = Scoreboard((R_SCORE_POS))
l_scoreboard = Scoreboard((L_SCORE_POS))

screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

play_on = True
while play_on:
    sleep(0.1)
    screen.update()
    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.hit_wall()

    contact_right_paddle = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    contact_left_paddle = ball.distance(l_paddle) < 50 and ball.xcor() < -320

    if contact_right_paddle or contact_left_paddle:
        ball.hit_paddle()
        
    left_score = right_score = 0
    if ball.xcor() > 390:
        left_score = l_scoreboard.add_scoreboard()
        ball.reverse()
    elif ball.xcor() < -390:
        right_score = r_scoreboard.add_scoreboard()
        ball.reverse()
    print(left_score)
    print(right_score)


screen.exitonclick()