'''
Faça um programa que leia 5 valores e guarde os em uma lista.
No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

listanum = list()
maior = menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]


print('-=' * 21)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posiçãões  ', end='')
for i, v in enumerate(listanum):#
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições  ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
print('-=' * 21)
# tentar com Max e Min e index