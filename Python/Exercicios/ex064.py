'''
Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar
o valor 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual a soma entre eles
(desconsiderando o flag)
'''
num = cont = soma = 0
num = int(input('Digite um número inteiro [999 para parar]: '))
while num != 999:
    soma+= num
    cont+=1
    num = int(input('Digite um número inteiro [999 para parar]: '))
print('='*55)
print('Você digitou {} números inteiros válidos.'.format(cont))
print('A soma do conjunto de números digitados é: {}'.format(soma))
print('=' * 55)