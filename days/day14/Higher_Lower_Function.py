from data import data
from random import choice
from logo import vs, logo
from replit import clear

#score = 0
def game():
    #global score
    score = 0
    firstPlayer = choice(data)
    secondPlayer = choice(data)
    if secondPlayer == firstPlayer:
        secondPlayer = choice
    print(logo)
    while True:
        print(f'Compare A: {firstPlayer.get("name")}, a {firstPlayer.get("description")} from {firstPlayer.get("country")}')
        print(vs)
        print(f'Compare B: {secondPlayer.get("name")}, a {secondPlayer.get("description")} from {secondPlayer.get("country")}')
        A = firstPlayer.get('follower_count')
        B = secondPlayer.get('follower_count')
        if A > B:
            max = A
        else:
            max = B
        question = input('Who has more followers? Type "A" or "B": ').strip().upper()
        if question == 'A' and max == A or question == 'B' and max == B:
            clear()
            score += 1
            print(logo)
            print(f'You\'re right, current score: {score}.')
        else:
            clear()
            print(f'Sorry, that\'s wrong! Final score: {score}.')
            exit(1)
        firstPlayer = secondPlayer
        if secondPlayer == firstPlayer:
            secondPlayer = choice(data)