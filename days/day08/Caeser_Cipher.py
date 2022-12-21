import my_cripto

codeOrDecode = input('Do you want to code or decode the message? ').lower()

if codeOrDecode == 'code':
    text = input('Enter the text you want to encrypt: ').lower()
    jumps = int(input('Enter the number of shifts: '))
    cipher = my_cripto.criptografar(text, jumps)
    print(f'Crypto message is: {cipher}')
    
elif codeOrDecode == 'decode':
    text = input('Enter the text you want to decript: ').lower()
    key = int(input('Enter the key to decript: '))
    clearText = my_cripto.decodificar(text, key)
    print(f'Decripted message is: {clearText}')


