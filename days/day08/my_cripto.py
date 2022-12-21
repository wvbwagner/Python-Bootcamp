import string

alpha = string.ascii_lowercase # the alphabet in lowercase
size = len(alpha)
def codeAlpha(shift):
    coding = ''
    startPoint = shift - size
    for i in range(startPoint, shift):
        coding += alpha[i]
    return str(coding)

def encryptMessage(text, shifts):
    localAlphabet = codeAlpha(shifts)
    encrypted = ''
    for letter in text:
        if letter not in alpha:
            encrypted += letter
        else:
            encrypted += localAlphabet[alpha.index(letter)]
    return encrypted

def decriptMessage(cipher, key):
    localAlphabet = codeAlpha(key)
    decripted = ''
    for letter in cipher:
        if letter not in alpha:
            decripted += letter
        else:
            decripted += alpha[localAlphabet.index(letter)]
    return decripted
