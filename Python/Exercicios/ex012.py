'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
'''

p = float(input('Digite o valor do produto: R$'))
d = p * 0.95
print("O produto custa R${:.2f}  e com 5% de desconto vai para: R${:.2f}".format(p, d))
