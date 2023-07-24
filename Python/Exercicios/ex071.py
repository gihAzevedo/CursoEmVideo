'''
Crie um programa que simule o funcionamento de um caixa eletrônico.No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
                MEU JEITO:
notas = conta = 0
print('='*48)
print('BANCO AZEVEDO'.center(48))
print('='*48)
while True:
    saque = float(input('Que valor você quer sacar? R$'))

    if saque >= 50:
        notas = saque//50
        saque -= (notas*50)
        print(f'Total de {notas:.0f} cédulas de R$50')
    if saque >=20:
        notas = saque//20
        saque -= (notas*20)
        print(f'Total de {notas:.0f} cédulas de R$20')
    if saque >=10:
        notas = saque // 10
        saque -= (notas*10)
        print(f'Total de {notas:.0f} cédulas de R$10')
    if saque >=1:
        notas = saque // 1
        print(f'Total de {notas:.0f} cédulas de R$1')
        break
print('='*48)
print('Volte sempre ao BANCO AZEVEDO! Tenha um bom dia!')
'''
print('=' * 30)
print('{:^30}'.format('BANCO AZEVEDO'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO AZEVEDO! Tenha um bom dia!')