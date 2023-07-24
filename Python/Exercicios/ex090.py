''' Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo na tela. '''
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['situação'] = ''
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items(): # Mostra cada item do aluno
    print(f'- {k} é igual a {v}')
