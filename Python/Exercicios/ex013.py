'''
Faça um algoritmo que leia salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

s = float(input('Digite o salário do funcionário: R$'))
a = s * 1.15
print('O salário atual do funcionário é de: R${:.2f}'.format(s))
print('Com o aumento de 15% vai para: R${:.2f}'.format(a))
