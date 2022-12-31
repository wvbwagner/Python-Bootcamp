from random import randint

def secretRandomNumber():
    return randint(1, 100)

def chooseLevel():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5
    return guesses

def checkWin(guess):
    global guesses
    if guess == secretNumber:
        print(f'You got it! The answer was {secretNumber}')
        exit(0)
    elif guess > secretNumber:
            print('Too high!')
            guesses -= 1
    elif guess < secretNumber:
            print('Too low!')
            guesses -= 1

def playerGuess():
    global guesses

    if guesses == 0:
        print('You\'ve run out of guesses. You lose!')
        exit(1)
        
    print(f'You have {guesses} attempts remaining to guess the number.')
    playerGuess = input('Make a guess: ')
    if playerGuess.isnumeric():
        return int(playerGuess)
    else:
        print('Not a valid number')
        exit(1)

def letsPlay():
    global secretNumber, guesses
    secretNumber = secretRandomNumber()
    guesses = chooseLevel()
    while True:
        checkWin(playerGuess())
        