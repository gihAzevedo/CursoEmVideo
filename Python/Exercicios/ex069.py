'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados
C) Quantas mulheres menores de 20 anos.
'''
maior = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        maior +=1
    if sexo == 'M':
        homem+=1
    if idade < 20 and sexo == 'M':
        mulher+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos  {mulher} mulheres com menos de 20 anos.')