'''
Refaça o DESAFRIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura While
'''
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
pa = primeiro
while cont != 10:
    print('{} →'.format(pa), end=' ')
    pa = pa +razao
    cont += 1
print('FIM')
