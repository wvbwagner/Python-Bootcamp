import string

alpha = string.ascii_lowercase # the alphabet in lowercase
size = len(alpha)

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