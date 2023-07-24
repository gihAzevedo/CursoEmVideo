'''
Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
cont = soma = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('--' * 20)
    computador = randint(0, 10)
    soma = jogador + computador
    resul = soma % 2
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ', end= '')
    print('PAR' if resul == 0 else 'ÍMPAR')
    print('--' * 20)
    if resul == 0 and tipo == 'P' or resul == 1 and tipo == 'I':
        cont+=1
        print('VOCÊ VENCEU! \nVamos jogar novamente...')
        print('=-' * 20)
    else:
        print('VOCÊ PERDEU!')
        print('=-' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes.')
