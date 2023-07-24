'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
totcompra = maiormil = baratoP = cont = 0
baratoN = ' '
print('-'*40)
print('LOJA AZEVEDO'.center(40))
print('-'*40)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if cont == 0 or preco < baratoP:
        baratoP = preco
        baratoN = produto
        cont+= 1
    totcompra += preco
    if preco > 1000:
        maiormil += 1
    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if seguir == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${totcompra}')
print(f'Temos {maiormil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratoN} que custa R${baratoP:.2f}')
