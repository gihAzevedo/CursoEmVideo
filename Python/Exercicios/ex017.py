'''
Faça um programa que leia o comprimento do cateto aposto e do cateto adjacente
de um triângulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
from math import hypot
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cat1, cat2)
print("A hipotenusa vai medir {:.2f}".format(hip))
