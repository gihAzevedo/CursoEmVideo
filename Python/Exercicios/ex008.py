'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
'''
m = float(input('Digite o tamanho em metro: '))
c = m * 100
mm = c * 10
print('O valor em metro é: {} \n Centimetros: {} \n Milimetro: {}'.format(m, c, mm))
