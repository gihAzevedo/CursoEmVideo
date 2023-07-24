'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual a será a base de conversão.
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
print('-=-'*10, ' BASE DE CONVERSÃO: ', '-=-'*10)
print('1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL')
base = int(input('Escolha a base de conversão: '))

if base == 1:
    print('O número inteiro \033[34m{}\033[m convertido para BINÁRIO fica \033[1:34m{}\033[m'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O número inteiro \033[34m{}\033[m convertido para OCTAL fica \033[1:34m{}\033[m'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O número inteiro \033[34m{}\033[m convertido para HEXADECIMAL fica \033[1:34m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[4:31mOPÇÃO INVÁLIDA. REINICIE O PROGRAMA E ESCOLHA ENTRE UMA DAS TRêS BASES.')