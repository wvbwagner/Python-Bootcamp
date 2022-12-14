import random, string
print('Welcome to the PyPassword Generator!')
letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like? '))
numbers = int(input('How many numbers would you like? '))

password = ''
tempPass = []
for i in range(0, letters):
    tempPass.append(random.choice(string.ascii_letters))
for i in range(0, symbols):
    tempPass.append(random.choice(string.punctuation))
for i in range(0, numbers):
    tempPass.append(random.choice(string.digits))
random.shuffle(tempPass)
for i in range(0, len(tempPass)):
    password += tempPass[i]
print(f'Your password is: {password}')

