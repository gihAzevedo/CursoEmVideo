'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça novamente até ter um valor correto.
'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo MASCULINO registrado com sucesso.')
else:
    print('Sexo FEMININO registrado com sucesso.')
