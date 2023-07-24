'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
07. e 08: Programa que pede números, diz o maior, soma e média
'''
soma = 0
maior = 0
print('-='*30)
for p in range(1, 6):
    num = float(input('{} -  Digite um número: '.format(p)))
    if num > maior:
        maior = num
    soma+=num
    media = soma / 5
print('-='*30)
print('O maior número do conjunto é: {:.1f}'.format(maior))
print('A soma do conjunto de números é: {:.1f}'.format(soma))
print('A média do conjunto de números é de: {:.1f}'.format(media))
print('-='*30)
