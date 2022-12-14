from random import randint
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
chosenName = names[randint(0, len(names) - 1)]
print(f'{chosenName} is going to buy the meal today!')

