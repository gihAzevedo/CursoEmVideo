'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
listacheia = []
par = []
impar = []

while True:
    listacheia.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção inválida! Tente novamente...')
    if resp == 'N':
        break
for i, v in enumerate(listacheia):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('-=' * 30)
print(f'Lista Completa: {listacheia}')
print(f'Lista de Números Pares: {par}')
print(f'Lista de Números Impares: {impar}')
print('-=' * 30)
