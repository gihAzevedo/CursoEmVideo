'''
Crie um programa que leia o nome de uma pessoa e mostre:
- O nome com todas as letras maiusculas.
- O nome com todas minúsculas.
- Quantas letras ao todos(sem considerar espaços)
- Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome ...........')
print('Todas letras em Maiscúlas: {}'.format(nome.upper()))
print('Todas as letras em Miniscúlas: {}'.format(nome.lower()))
print('O nome: {} possui {} letras'.format(nome, len(nome) - nome.count(' ')))
print('O primeiro nome possui {} letras'.format(nome.find(' ')))




