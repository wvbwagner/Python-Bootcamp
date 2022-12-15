def turn_right():
    for i in range(3):
        turn_left()
def facesNorth():
    while not is_facing_north():
        turn_left()
def checkRight():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right() and not wall_in_front():
        for i in range(1):
            move()
    elif right_is_clear() and not wall_in_front():
        for i in range(1):
            turn_right()
            move()
    elif not wall_on_right() and wall_in_front():
        turn_right()
        for i in range(1):
            move()
    else:
        checkFront()
def checkFront():
    while True:
        if wall_in_front():
            turn_left()
        elif not wall_in_front():
            for i in range(1):
                move()
        else:
            checkRight()
while not at_goal():
    #facesNorth()
    checkRight()

    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
