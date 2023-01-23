import pandas
from turtle import Turtle, Screen
from scoreboard import Scoreboard

us_states = pandas.read_csv("us-states-game-start/50_states.csv")

screen = Screen()
screen.setup(width=750, height=550)
screen.title("U.S. States Game")
gif = "us-states-game-start/blank_states_img.gif"
screen.addshape(gif)

turtle = Turtle()
turtle.shape(gif)

scoreboard = Scoreboard()

states = us_states['state'].tolist()
get_x = us_states['x'].tolist()
get_y = us_states['y'].tolist()
already_answered = []

while len(already_answered) < len(states):
    in_list = screen.textinput(f"{scoreboard.score}/{len(states)} Correct", "Type in a state: ").title()
    if in_list in states:
        pos = states.index(in_list)
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.setpos(get_x[pos], get_y[pos])
        turtle.write(in_list, align='center', font=("Arial", 9, 'normal')) 
        if in_list not in already_answered:
            scoreboard.update_score()
            already_answered.append(in_list)
    elif in_list == 'Exit':
        break

missing = []
for state in states:
    if state not in already_answered:
        missing.append(state)

not_listed = {'Missing': missing}
dict = pandas.DataFrame(not_listed)
dict.to_csv('us-states-game-start/Missing_States.csv')

screen.exitonclick()

