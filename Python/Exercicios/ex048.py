'''
Faça um porgrama que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
cont = 0
for c in range(0, 500, 3):
    modulo = c%2
    if modulo ==1:
        cont+=1
        s+= c
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
