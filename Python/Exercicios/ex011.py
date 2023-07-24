'''
Faça um programa que leia a altura e a largura de uma parede em metros,
calcule sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
'''

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
mq = alt * lar
lt = mq / 2

print('='*90)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lar, alt, mq))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(lt))
