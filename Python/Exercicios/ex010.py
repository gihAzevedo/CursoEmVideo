'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere
US$ = 1,00 = R$3,27
'''
r = float(input('Digite qual o valor que você possui em real: '))
d = float(input('Qual o valor do Dólar atualmente: '))
c = r / d
print('-'*70)
print('Você possui: R$ {} \nO dólar está em: US$: {} \n Sendo assim você pode comprar: US$ {:.2f}'.format(r, d, c))
