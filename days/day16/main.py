from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while True:
    order = input(f'What would you like to drink: {menu.get_items()} ').strip().lower()
    if order == 'report':
        coffe_maker.report()
        money_machine.report()
    elif order == 'off':   
        print('Shutting down...')
        sleep(1)
        exit(1)
    else:
        drink = menu.find_drink(order)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
            
