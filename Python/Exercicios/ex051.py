'''
Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros dessa progressão.
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 9 * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end=' ')
print('ACABOU')
