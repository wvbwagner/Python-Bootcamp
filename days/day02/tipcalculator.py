print('Welcome to the Tip calculator')
bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))
total = (bill / people) +  bill / people * tip / 100
print(f'Each person should pay ${total:.2f}')