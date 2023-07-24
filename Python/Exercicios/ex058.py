'''
Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
computador = randint(0, 10)  # Faz o computador pensar
acertou = False
cont = 1
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    if jogador == computador:
        print('*-*'*20)
        print('PARABÉNS! VOCÊ GANHOU!'.center(60))
        print('Você precisou de {} tentativas para me vencer.'.format(cont).center(60))
        print('*-*' * 20)
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
        cont += 1