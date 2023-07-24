'''
Faça um programa que mostre a tabuada de vários números, um decada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if n < 0:
        for c in range(0, 11):
            mult = n * c
            print(f'{n} X {c:2} = {mult}')
        print('-' * 35)
    else:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
