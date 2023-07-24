'''
# Primeiro parâmetro é onde inicia; Segundo parâmetro onde termina a contagem; terceiro parâmetro é sobre qual ordem seguir.
for c in range(6, 0, -1):
# print('Oi')
    print(c)
print('FIM')

# Parametros escolhidos pelo usuário:
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
