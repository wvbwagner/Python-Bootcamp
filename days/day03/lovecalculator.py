name1 = input('What is your name? \n').upper()
name2 = input('What is their name? \n').upper()
cont = 0
word = 'TRUE'
for i in word:
    cont += name1.count(i) + name2.count(i)
total = str(cont)
cont = 0
word = "LOVE"
for i in word:
    cont += name1.count(i) + name2.count(i)
total  += str(cont)
total = int(total)
if total < 10 or total > 90:
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total > 40 and total < 50:
    print(f'Your score is {total}, you are aright together.')
else:
    print(f'Your score is {total}.')

    

        