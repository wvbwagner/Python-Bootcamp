ano = int(input('Which year do you want to check: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Leap year.')
else:
    print('Not a leap year.')