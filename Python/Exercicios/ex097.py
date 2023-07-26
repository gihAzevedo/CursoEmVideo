'''
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:  escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
'''


def escreva(texto):
    print('~' * (len(texto)+4))
    print(f'  {texto}')
    print('~' * (len(texto)+4))


#Programa Principal
mensagem = str(input('Digite sua mensagem: '))
escreva(mensagem)
