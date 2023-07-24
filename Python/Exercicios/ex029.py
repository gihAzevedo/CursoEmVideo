'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite

RESOLUÇÃO GUANABARA:
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
        print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
        multa = (velocidade - 80) * 7
        print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
'''
velocidade = float(input("Qual a velocidade do carro? "))
if velocidade >80:
    multa = (velocidade-80)*7
    print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE ESTABELCIDO EM 80km/h')
    print('O valor da multa é de: R${:.2f}'.format(multa))
else:
    print('VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE')
    print('NÃO HÁ MULTA PARA PAGAR!')

