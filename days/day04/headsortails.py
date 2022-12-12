from random import randint, choice
# coin variable receives a random number between 0 and 1
coin = randint(0, 1)
if coin == 0:
    print('Heads')
elif coin == 1:
    print('Tails')
