from time import sleep 
print('Bem vindos ao jogo da Ilha do Tesouro!\nSua missão é encontrar o tesouro!')
print('Existem dois caminhos a sua frente. Para onde você quer ir? ')
direcao = input('Digite "E" para ir para a esquerda ou "D" para ir para a direita: ').strip().upper()
if direcao == 'E':
    print('Depois de muito andar, você chegou a beira de um lago. E no meio do lago é possível ' + 
    'ver uma ilha.')
    ilha = input('Você quer esperar por uma canoa para te levar até ilha ou quer nadar? ' + 
    'Digite "N" para nadar ou "B" para esperar o barco: ').strip().upper()
    if ilha == 'B':
        print('Você finalmente chegou a ilha. E nela existem três portas: uma amarela, uma azul' +
        ' e outra vermelha')
        porta = input('Qual porta você quer abrir? Digite "A" para amarela, "Z" para azul e ' + 
        '"V" para vermelha: ').strip().upper()
        if porta  == 'A':
            print('Você abriu a porta...', end=' ')
            sleep(1)
            print('e foi atacada por um leão e morreu.\nFIM DE JOGO')
        elif porta == 'Z':
            print('Você abriu a porta...', end=' ')
            sleep(1)
            print('e ao entrar caiu em areia movediça e morreu!\nFIM DE JOGO')
        elif porta == 'V':
            print('Você abriu a porta...', end=' ')
            sleep(1)
            print('e ao entrar encontrou o tesouro perdido do dragão!!\nPARABÉNS, VOCÊ VENCEU')
        else:
            print('A escolha que você fez não existe.\nFIM DE JOGO')
    elif ilha == 'N':
        print('O a agua do lago era muito fria...e você foi nadando...')
        sleep(1)
        print('E nadando...')
        sleep(1)
        print('E foi atacado pelo monstro do lago e morreu"\nFIM DE JOGO')
    else:
        print('A escolha que você fez não existe.\nFIM DE JOGO')
elif direcao == 'D':
    print('Esse caminho vai descendo...')
    sleep(1)
    print('E ficando cada vez mais escuro...')
    sleep(1)
    print('E descendo...até que você caiu em um buraco enorme e morreu!\nFIM DE JOGO!')
else:
    print('A escolha que você fez não existe.\nFIM DE JOGO')
