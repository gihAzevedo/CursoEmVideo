'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o \033[1:32mPRIMEIRO\033[m valor: '))
n2 = int(input('Digite o \033[1:33mSEGUNDO\033[m valor: '))
if n1 > n2:
    print('O \033[1:32mPRIMEIRO\033[m valor é MAIOR.')
elif n2 > n1:
    print('O \033[1:33mSEGUNDO\033[m valor é MAIOR.')
else:
    print('Os dois valores são \033[1:36mIGUAIS\033[m.')