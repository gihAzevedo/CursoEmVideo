'''
Faça um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    pessoa = int(input('{} - Digite o ano de nascimento: '.format(c)))
    conta = atual - pessoa
    if conta >= 21:
        maior+= 1
    else:
        menor+=1
print('{} pessoas ATINGIRAM a maioridade.'.format(maior))
print('{} pessoas NÃO ATINGIRAM a maioridade.'.format(menor))
