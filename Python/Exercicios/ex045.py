# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 20)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 20)

    if computador == jogador:
        print('EMPATE')
    elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
        print('JOGADOR VENCE')
    elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
        print('COMPUTADOR VENCE')
else:
    print('-=' * 20)
    print('OPÇÃO INVÁLIDA! REINICIE O JOGO.')
    print('-=' * 20)
