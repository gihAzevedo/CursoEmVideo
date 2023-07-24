'''
Escreva um programa que faça o computador "pensar" em um numero inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu

'''

from random import randint

sorteio = randint(0, 5)
numero = int(input('Digite um número entre 0 e 5: '))
print('O número que o computador pensou foi: {}'.format(sorteio))
if sorteio == numero:
    print('VOCÊ ADIVINHOU O NÚMERO QUE O COMPUTADOR PENSOU. PARABÉNS!')
else:
    print('TENTE NOVAMENTE! DESSA VEZ VOCÊ ERROU!')
'''
RESOLUÇÃO GUANABARA:
from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
'''