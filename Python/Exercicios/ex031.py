'''
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e
R$0,45 para viagens mais longas.
'''
distancia = float(input("Quantos é a distância da sua viagem? "))
print('Você esta prestes a começar uma viagem de {} Km'.format(distancia))
if distancia <=200:
    val = distancia * 0.5
else:
    val = distancia * 0.45

#(FORMA SIMPLIFICADA) val = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(val))
