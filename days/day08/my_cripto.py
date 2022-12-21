def entradaUsuario(choice):
    if choice == 'code':    
        text = input('Enter the text you want to encrypt: ')
        jumps = int(input('Enter the number of shifts: '))
        return codificador(text, jumps)

    elif choice == 'decode':
        text = input('Enter the text you want to decript: ')
        key = int(input('Enter the key to decript: '))
        return decodificador(text, key)

    else:
        return "Invalid entry"
        exit(1)

def codificador(texto, passo):
    codigo = ''
    for letra in texto:
        codigo += chr((ord(letra) + passo))
    return codigo

def decodificador(cipher, passo):
    clear = ''
    for letra in cipher:
        clear += chr((ord(letra) - passo))
    return clear