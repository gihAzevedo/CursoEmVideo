'''
Um professor quer sortear entre seus 4 alunos para apagar o quadrado.
Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome escolhido
'''
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno que irá apagar o quadro é o: {}'.format(sorteio))
