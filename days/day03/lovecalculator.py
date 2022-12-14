name1 = input('What is your name? \n')
name2 = input('What is their name? \n')
cont = 0
word = 'TRUE'
names = (name1 + name2).upper()
for i in word:
    cont += names.count(i)
total = str(cont)
cont = 0
word = 'LOVE'
for i in word:
    cont += names.count(i)
total += str(cont)
total = int(total)
if total < 10 or total > 90:
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total > 40 and total < 50:
    print(f'Your score is {total}, you are alright together.')
else:
    print(f'Your score is {total}.')
        
