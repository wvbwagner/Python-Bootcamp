import my_cripto

codeOrDecode = input('Do you want to code or decode the message? ').lower()

mensagem = my_cripto.entradaUsuario(codeOrDecode)
print(mensagem)