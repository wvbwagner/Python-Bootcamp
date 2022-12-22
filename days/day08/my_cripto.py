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
        if letter not in alpha:
            cipher += letter
        else:
            cipher += (alpha[alpha.index(letter) - passoReal])
    return str(cipher)
    
def decodificar(texto, passo):
    clear = ''
    for letter in texto:
        if letter not in alpha:
            clear += letter
        else:
            clear += (alpha[alpha.index(letter) - passo])
    return str(clear)