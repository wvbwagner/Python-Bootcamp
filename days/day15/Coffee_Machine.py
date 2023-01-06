import locale
from time import sleep

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

itens = {
 'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'price': 1.5},
 'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'price': 2.5}, 
 'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'price': 3.0}
}

ingredients = {'water': 300, 'milk': 200, 'coffee': 100}


PENNY = 0.01
NICKEL = 0.05
DIME = 0.1
QUARTER = 0.25

def getReport(money):
    '''Prints the total of ingredients available, as well as the total profit'''
    print(f'Water: {ingredients.get("water")}ml')
    print(f'Milk: {ingredients.get("milk")}ml')
    print(f'Coffee: {ingredients.get("coffee")}g')
    print(locale.currency(money))

def setReport(order):
    '''Decreases the amount of ingredients available and sets the new values'''
    ingredients['water'] -= itens[order].get('water')
    ingredients['milk'] -= itens[order].get('milk')
    ingredients['coffee'] -= itens[order].get('coffee')
    return ingredients

def checkResources(order):
    '''Checks if the amount of ingrediens available is enough; returns True if so, False if not so'''
    water = ingredients.get('water')
    milk = ingredients.get('milk')
    coffee = ingredients.get('coffee')
    if water >= itens[order].get('water') and milk >= itens[order].get('milk'):
        if coffee >= itens[order].get('coffee'):
            return True
    elif water < itens[order].get('water'):
        print('Not enough water')
    elif milk < itens[order].get('milk'):
        print('Not enough milk')
    elif coffee < itens[order].get('coffee'):
        print('Not enough coffee')
    return False


def checkMoney(order):
    '''Receives the amount of money and checks if it is enough to pay for the item; returns the value
    of the item so it can be added to the profit. Also calls for setReport() to set the new amount of
    ingredients'''
    print('Please insert coins.')
    price = itens[order].get('price')
    quarter = int(input('How many quarters? ')) * QUARTER
    dimes = int(input('How many dimes? ')) * DIME
    nickles = int(input('How many nickles? ')) * NICKEL
    pennies = int(input('How many pennies? ')) * PENNY
    sum = quarter + dimes + nickles + pennies
    if sum >= price:
        print(f'Here is {locale.currency(sum - price)} in change.\nEnjoy your {order}!')
        setReport(order)
        return price
    else:
        print(f'Not enough money, refunding {locale.currency(sum)}')
        return 0.0


def cafe():
    profit = 0
    while True:
        ask = input('What would you like? (espresso/latte/cappuccino) ')
        if ask == 'report':
            getReport(profit)
        elif ask == 'off':
            print('Shutting down...')
            sleep(1)
            exit(1)
        elif ask not in itens:
            print('Invalid choice')
        elif checkResources(ask):
            profit += checkMoney(ask)
        

cafe()