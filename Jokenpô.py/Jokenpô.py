from random import randint
itens = ('pedra', 'papel', 'tesoura ')
computador = randint (0,2)
print('''suas opções são 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('qual sua jogada?'))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('DEU EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('DEU EMPATE')
    else:
        print('OPÇÃO INVALIDA')
