'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

listanum = list()
while True:
    listanum.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção Inválida! Tente novamente.')
    if resp == 'N':
        break

listanum.sort(reverse= True)
print('-=' * 30)
print(f'Você digitou {len(listanum)} elementos.')
print(f'Os valores em ordem decrescente são: {listanum}')
if 5 in listanum:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
print('-=' * 30)
