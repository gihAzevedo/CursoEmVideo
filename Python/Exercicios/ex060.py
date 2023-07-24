'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex:
5! = 5 X 4 X 3 X 2 X 1= 120
'''
'''                 MEU JEITO

num = int(input('Digite um número para saber seu fatorial: '))
fat = guardar = num

while num != 1:
    fat = fat * (num - 1)
    num -= 1

print('{}! é: {}'.format(guardar, fat))
    
               1º RESOLUÇÃO GUANABARA
               
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''
n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1
print('{}'.format(f))
