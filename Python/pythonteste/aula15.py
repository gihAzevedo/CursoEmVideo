'''n = s = 0
while True:
    n =  int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # Trabalhando com f string
'''
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}') # PYTHON 3.6 +

'''
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
'''