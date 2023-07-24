'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro,ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adiconado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção Inválida! Tente novamente.')
    if resp == 'N':
        break

print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
