'''
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
'''
cont = 0
s = 0
for c in range(1,7):
    n = int(input('{} - Digite um número: '.format(c)))
    modulo = n % 2
    if modulo == 0:
        s+= n
        cont+=1
print('Você informou {} números PARES e a soma foi {}'.format(cont, s))
