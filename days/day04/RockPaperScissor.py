import random
from time import sleep

item = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = random.randint(0, 2)

while True:
    player = int(input('Qual a sua jogada?\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n'))
    if player < 0 or player > 2:
        print('Valor inválido!')
    else:
        break

print('\nPEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
print(f'\nComputador jogou {item[cpu]}')
print(f'Você jogou {item[player]}')
if cpu == player:
    print('Empate')
elif item[cpu - 1] == item[player]:
    print('COMPUTADOR venceu!') 
else:
    print('JOGADOR venceu!')
