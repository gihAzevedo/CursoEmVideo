'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
numero = int(input('Digite um número inteiro: '))
conta = numero % 2
if conta == 0:
    print('O número: {} é PAR'.format(numero))
else:
    print('O número: {} é IMPAR'.format(numero))

