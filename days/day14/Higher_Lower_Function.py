from data import data
from random import choice
from logo import vs, logo
from replit import clear

score = 0
storePlayer = {}
def initialPlay(score):
    global storePlayer
    if score == 0:
        player1 = choice(data)
        player2 = choice(data)
        if player2 == player1:
            player2 = choice(data)
    else:
        player1 = storePlayer
        player2 = choice(data)
        if player2 == player1:
            player2 = choice(data)
    storePlayer = player2
    return player1, player2

def presentPlayers(score):
    firstPlayer, secondPlayer = initialPlay(score)
    print(f'Compare A: {firstPlayer.get("name")}, a {firstPlayer.get("description")} from {firstPlayer.get("country")}')
    print(vs)
    print(f'Compare B: {secondPlayer.get("name")}, a {secondPlayer.get("description")} from {secondPlayer.get("country")}')
    playerOne = firstPlayer.get('follower_count')
    playerTwo = secondPlayer.get('follower_count')
    if playerOne > playerTwo:
        max = playerOne
    else:
        max = playerTwo
    return playerOne, playerTwo, max

def comparePlayers(valuesToCompare):
    global score
    playerOne, playerTwo, maximum = valuesToCompare
    question = input('Who has more followers? Type "A" or "B": ').strip().upper()
    if question == 'A' and maximum == playerOne or question == 'B' and maximum == playerTwo:
        clear()
        score += 1
        print(logo)
        print(f'You\'re right, current score: {score}.')
    else:
        clear()
        print(f'Sorry, that\'s wrong! Final score: {score}.')
        exit(1)

def play():
    print(logo)
    while True:
        comparePlayers(presentPlayers(score))