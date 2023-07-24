from random import randint
carta1 = randint(1, 10)
carta2 = randint(1, 10)
cartaM = 0
somarM = 0
somarM = carta1 + carta2
print(f'Maria Luiza suas cartas são: {carta1} e {carta2}.')
resp = ' '
while resp not in 'SN':
    resp = str(input('Deseja puxar mais uma carta? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    if resp == 'S':
        cartaM = randint(1, 10)
        print(f'A carta puxada do baralho foi: {cartaM}')
        somarM += cartaM
        resp = ' '
        if somarM > 21:
            print('-=' * 45)
            print(f'VOCÊ ESTOUROU!')
            break
        elif somarM == 21:
            break
    else:
        print('OPÇÃO INVÁLIDA! Tente Novamente...')
print('-=' * 45)
computador = randint(2, 30)
if somarM > computador and somarM <= 21:
    print('MALU GANHOU!!!')
elif somarM == computador:
    print('MARIA LUIZA E COMPUTADOR EMPATARAM!!!')
elif somarM < computador and computador <= 21 or (somarM >computador and computador <=21):
    print('COMPUTADOR GANHOU!!!')
elif somarM and computador > 21:
    print('Ninguém ganhou!!!')
print(f'MALU: {somarM} PONTOS.\nComputador: {computador} PONTOS')
