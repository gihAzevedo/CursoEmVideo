'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
data = date.today().year

print('#='*10, 'ALISTAMENTO OBRIGATÓRIO', '=#'*10)
genero = int(input('''
[1] - Mulher
[2] - Homem
Escolha uma das opções acima: '''))
print('#='*30)
if genero == 1:
    print('O alistamento NÃO É OBRIGATÓRIO para MULHERES.')
elif genero == 2:
    print('O alistamento é OBRIGATÓRIO para HOMENS!')

    nascimento = int(input('Ano de nascimento: '))
    idade = data - nascimento
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, data))
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format((18 - idade)))
        print('Seu alistamento será em {}.'.format(nascimento + 18))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(nascimento + 18))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('OPÇÃO INVÁLIDA! REINICIE O PROGRAMA E TENTE NOVAMENTE.')


