def add(*args):
    return sum(args)

numeros = add(9, 7, 6, 35, 42)
print(numeros)


def calculator(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculator(2, add= 3, multiply= 5)
#print(num)