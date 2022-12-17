from random import choice
import string
import hangman_word, hangman_drawings
from replit import clear

chances = 6
escolha = choice(hangman_word.vocabulario)
palavra = []
for letra in escolha:
	palavra.append('_')
tentadas = []
while True:
	print('\n' + '-#' * 20 + '\n')
	print(f'Letras já usadas: {tentadas}')
	print(f'Chances: {chances}')
	print(hangman_drawings.draw[chances])
	for letra in palavra:
		print(letra, end=' ')
	palpite = input("Digite seu palpite ou 'SAIR' para sair do programa: ").upper()
	clear()
	if palpite == 'SAIR':
		break

	if palpite in tentadas:
		print('\n\033[1;35mVocê já tentou essa letra!\033[m')
		continue
	tentadas.append(palpite)

	if palpite in escolha:
		print("\n\033[1;32mBoa, tem a letra!\033[m\n")
	else:
		chances -= 1
		print('\n\033[1;31mNão tem essa letra na palavra.\033[m\n')
		if chances == 0:
			print(hangman_drawings.draw[chances])
			print("\n\033[1;33mFIM DE JOGO!\033[m\n")
			break
	for i in range(len(palavra)):
		if escolha[i] == palpite:
			palavra[i] = palpite
	
	if '_' not in palavra:
				print('\033[1;34mPARABÉNS, VOCÊ VENCEU!\033[m\n')
				break
