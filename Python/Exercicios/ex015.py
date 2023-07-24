'''
Escreva um programa que leia a quantidade de km percoridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por km rodado.
'''
dia = int(input('Quantos dias alugados? '))
km = float(input("Quantos Km rodados? "))

diap = dia*60
kmp = km * 0.15
total = diap + kmp
print("O total a pagar é de: R${:.2f}".format(total))
