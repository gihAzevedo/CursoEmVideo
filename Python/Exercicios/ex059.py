'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
from time import sleep
soma =  mult = maior= 0
opcao = 4
while opcao!= 5:
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('-=-' * 20)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair 
    '''.ljust(1))
    opcao = int(input('>>>>> Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1>= n2:
           maior = n1
        else:
            maior = n2
        print('Entre {} e {} o MAIOR valor é {}'.format(n1, n2, maior))
    elif opcao >=6:
        print('Opção Inválida. Tente novamente')
if opcao == 5:
    print('Finalizando...')
    sleep(1)
    print(('-=-'*20))
    print('Fim do Programa! Volte sempre!')
