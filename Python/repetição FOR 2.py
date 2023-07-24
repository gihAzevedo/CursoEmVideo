'''
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
'''
primeiro = int(input('Digite um número inteiro: '))
segundo = int(input('Digite outro numéro inteiro: '))
print('= '*20)
print('\033[33m{}\033[m'.format(primeiro), end= ' ')
for c in range (primeiro+1, segundo):
    print('{}'.format(c), end= ' ')
print('\033[33m{}'.format(segundo))
