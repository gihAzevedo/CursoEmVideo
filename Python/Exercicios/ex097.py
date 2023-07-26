'''
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:  escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
'''

def mensagem(texto):
    print('~' * len(texto))
    print(f'{texto}')
    print('~' * len(texto))


recado = str(input('Digite sua mensagem: '))
mensagem(recado)
