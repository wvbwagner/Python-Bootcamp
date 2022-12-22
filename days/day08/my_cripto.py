import string

alpha = string.printable
size = len(alpha)

def entradaUsuario(choice):
    if choice == 'code':    
        text = input('Enter the text you want to encrypt: ')
        jumps = int(input('Enter the number of shifts: '))
        return criptografar(text, jumps)

    elif choice == 'decode':
        text = input('Enter the text you want to decript: ')
        key = int(input('Enter the key to decript: '))
        return decodificar(text, key)

    else:
        return "Invalid entry"
        exit(1)

def criptografar(texto, passo):
    cipher = ''
    passoReal = size - passo
    for letter in texto:
        position = alpha.index(letter)
        newPosition = position - passoReal
        cipher += alpha[newPosition]
    return str(cipher)
    
def decodificar(texto, passo):
    clear = ''
    for letter in texto:
        position = alpha.index(letter)
        newPosition = position - passo
        clear += alpha[newPosition]
    return str(clear)