from random import choice
from replit import clear

'''
Regras:
Acima de 21, perde
Abaixo de 17, obrigatório outra carta
A: vale 1 ou 11, vc escolhe
J, Q, K: valem 10
'''
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def dealCards():
    # returns a random card from the deck
    return choice(cards)

def myCards():
    # gives two cards to the player
    myCards = []
    for i in range(2):
        myCards.append(dealCards())
    return myCards

def cpuCards():
    # gives cards to the computer until it has a minimum score of 17
    global cpuPoints
    cpuCards = []
    cpuPoints = sum(cpuCards)
    while cpuPoints <  17:
        cpuCards.append(dealCards())
        cpuPoints = sum(cpuCards)
    return cpuCards

'''myHand = myCards()
myPoints = sum(myHand)
cpuHand = cpuCards()'''

def startGame():
    global myPoints, myHand, cpuHand
    myHand = myCards()
    myPoints = sum(myHand)
    cpuHand = cpuCards()
    while True:
        print(f'Your cards are {myHand}. Your score is {myPoints}')
        print(f'Computer\'s first card is {cpuHand[0]}')
        question = input("Type 'y' to get another card, type 'n' to pass: ")
        if question == 'y':
            myHand.append(dealCards())
            myPoints += myHand[-1]
            if myPoints > 21:
                break
        else:
            break
    checkResults()

def checkResults():
    print(f'Your final hand is {myHand}, final score: {myPoints}')
    print(f'Computer\'s final hand is {cpuHand}, final score: {cpuPoints}')
    if myPoints > 21:
        print('You went over. You lose!')
    elif cpuPoints > 21 and myPoints < 21:
        print('CPU went over. You win!')
    elif cpuPoints > myPoints:
        print('You lose!')
    elif cpuPoints < myPoints:
        print('You win!')
    elif cpuPoints == myPoints:
        print('It\'s a draw')

def wannaPlay():
    play = True
    while play:
        question = input('Do you want to play BlackJack Capstone: [y] [n] ')
        if question == 'y':
            clear()
            #myHand.clear()
            #cpuHand.clear()
            startGame()
        elif question == 'n':
            print('Good bye!')
            exit(0)
        else:
            print('Invalid answer')
