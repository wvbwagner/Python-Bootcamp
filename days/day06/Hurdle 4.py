def turn_right():
    for i in range(3):
        turn_left()
def jumpUp():
    if wall_in_front():
        turn_left()
        while wall_on_right():
            move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
def path():
    if front_is_clear():
        move()
    else:
        jumpUp()
while not at_goal():
   path()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
