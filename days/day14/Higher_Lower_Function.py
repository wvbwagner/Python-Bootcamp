from data import data
from random import choice
from logo import vs, logo
from replit import clear

storePlayer = {}
def initialPlay(score):
    global storePlayer
    if score == 0:
        player1 = choice(data)
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
    
    return playerOne, playerTwo

def comparePlayers(valuesToCompare, score):
    playerOne, playerTwo = valuesToCompare
    if playerOne > playerTwo:
        maximum = playerOne
    else:
        maximum = playerTwo
    question = input('Who has more followers? Type "A" or "B": ').strip().upper()
    if question == 'A' and maximum == playerOne or question == 'B' and maximum == playerTwo:
        clear()
        score += 1
        print(logo)
        print(f'You\'re right, current score: {score}.')
        return score
    else:
        clear()
        print(f'Sorry, that\'s wrong! Final score: {score}.')
        exit(1)

def play():
    score = 0
    print(logo)
    while True:
        score = comparePlayers(presentPlayers(score), score)