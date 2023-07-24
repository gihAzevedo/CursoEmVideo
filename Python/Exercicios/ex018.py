'''
Faça um programa que leia um ângulo qualque e mostre na tela o seno, cosseno e tangente
'''
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {} tem o Seno de: {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o Cosseno de: {:.2f}'.format(ang, cosseno))
print(('O ângulo de {} tem a Tangente de: {:.2f}'.format(ang, tangente)))
