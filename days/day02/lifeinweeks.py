age = input("What is your current age? ")

# o que é 90?
days = 90 * 365
weeks = 90 * 52
months = 90 * 12

age = int(age)

# o que é dleft wleft e mleft?
dleft = days - age * 365
wleft = weeks - age * 52
mleft = months - age * 12

print(f'You have {dleft} days, {wleft} weeks, and {mleft} months left.') 