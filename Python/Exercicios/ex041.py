'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre dsua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print('O atlteta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade<= 19:
    print('Classiicação: JUNIOR')
elif idade <=25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
