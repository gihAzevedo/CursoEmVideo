''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. '''
def voto(nascimento):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - nascimento
    if idade < 16:
        op = 'NÃO VOTA!'
    elif idade >= 16 and idade < 18 or idade > 70:
        op = 'VOTO OPCIONAL.'
    elif idade > 18 and idade <= 70:
        op = 'VOTO OBRIGATÓRIO!'
    print(f'Com {idade} anos: {op}')

# Programa Principal
print('--' * 15)
ano = int(input('Em que ano você nasceu? '))
voto(ano)

