import my_cripto

codeOrDecode = input('Do you want to code or decode the message? ').lower()

if codeOrDecode == 'code':
    text = input('Enter the text you want to encrypt: ').lower()
    jumps = int(input('Enter the number of shifts: '))
    textSize = len(text)
    print(f'Crypto message is: {my_cripto.encryptMessage(text, jumps)}')
elif codeOrDecode == 'decode':
    text = input('Enter the text you want to decript: ').lower()
    key = int(input('Enter the key to decript: '))
    print(f'Decripted message is: {my_cripto.decriptMessage(text, key)}')


