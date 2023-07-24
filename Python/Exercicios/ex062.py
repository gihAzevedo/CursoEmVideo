'''
Melhore o DESAFIO 061, perguntando se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
pa = primeiro
seguinte = 10
termos = 0
while seguinte!=0:
    termos+= seguinte
    if seguinte != 0:
        while cont != seguinte:
            print('{}'.format(pa), end=' ')
            pa = pa +razao
            cont += 1
    print('PAUSA')
    if cont == seguinte:
        cont = 0
        seguinte = int(input('\nDeseja mostrar mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados.'.format(termos))
