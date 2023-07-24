'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execeução, mostre a média entre todos os valores e qual foi o maior e o menor valores digitados.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


'''         MEU JEITO
prosseguir = 'S'
cont = media = maior = soma = menor = 0
while prosseguir == 'S':
    num = float(input('Digite um número: '))
    if cont == 0:
        menor = num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    soma+=num
    cont+=1
    media = soma / cont
    prosseguir = str(input('Deseja digitar mais um número? [S/N] ')).upper().strip()[0]
else:
    print('=' * 55)
    print('Foram digitados {} números e a média entre eles é {}'.format(cont, media))
    print('MAIOR número digitado: {}'.format(maior))
    print('MENOR número digitado: {}'.format(menor))
    print('=' * 55)
'''