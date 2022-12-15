def jumpOver():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jumpOver()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
