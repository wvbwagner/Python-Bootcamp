age = input("What is your current age? ")
# all calculations done with 90 as the maximum age
days = 90 * 365
weeks = 90 * 52
months = 90 * 12
age = int(age)
daysLeft = days - age * 365
weeksLeft = weeks - age * 52
monthsLeft = months - age * 12
print(f'You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.') 
