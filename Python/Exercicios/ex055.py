'''
Faça um programa que leia o peso de cinco pessoas. No final mostre qual o maior e o menor peso.
'''
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('{} - Digite o seu peso (Kg): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso <= menor:
            menor = peso
        if peso >= maior:
            maior = peso
print('O MAIOR peso foi: {} Kg'.format(maior))
print('O MENOR peso foi: {} Kg'.format(menor))
