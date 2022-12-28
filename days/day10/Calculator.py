
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    num1 = float(input('Enter the first number: '))
    toContinue = True
    while toContinue:
        operator = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
        }
        for symbols in operator:
            print(symbols)
        operation = input('Pick the desired operation: ')
        num2 = float(input('Enter the next number: '))
        result = operator.get(operation)(num1, num2)
        print(f'{num1} {operation} {num2} = {result}\n')
        question =  input(f'''Type "yes" to use {result} for another calculation, "no" to start over 
with new values or "stop" to stop calculating: ''').strip().lower()
        if question == 'yes':  
            num1 = result
        elif question == 'no':
            toContinue = False
            calculator()
        elif question == 'stop':
            exit(0)
        else:
            print("Invalid answer")
            exit(1)
calculator()