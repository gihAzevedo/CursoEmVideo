'''
Escreva um programa que leia um número N qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos voc~e quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont=3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')

'''     MEU JEITO
cont = num1 = num2 = fib = 0
print('='*30)
print('SEQUÊNCIA FIBONACCI'.center(30))
print('='*30)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
while cont!= termos:
    if cont == 0:
        print('{} →'.format(fib), end=' ')
        fib+=1
        num1+=1
    else:
        print('{} →'.format(fib), end=' ')
        fib = num1 + num2
        num2 = num1
        num1 = fib
    cont+=1
print('FIM')
print('~'*30)
'''
'''
num = int(input('Digite um número: '))
elementos = int(input('Digite quantos elementos deseja: '))
num2 = 0
num3 = 0
while cont != elementos:
    if num!= 0:
        print('{} →'.format(num), end=' ')
        num3 = num + num2
        num2 = num
        num = num3
        cont+=1
    else:
        print('{} →'.format(num), end=' ')
        num = 1
        cont+=1
print('FIM')
'''