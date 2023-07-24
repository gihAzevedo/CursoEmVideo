'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurdo de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais.
- Isósceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')