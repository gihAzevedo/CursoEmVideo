'''
 Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS AZEVEDO '))
preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = preco*0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto))
    print('Seu desconto foi de: R${:.2f}'.format(preco*0.1))
elif opcao == 2:
    desconto = preco*0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto))
    print('Seu desconto foi de: R${:.2f}'.format(preco * 0.05))
elif opcao == 3:
    parcelas = preco / 2
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preco, parcelas))
elif opcao == 4:
    qtde = int(input('Quantas parcelas? '))
    parcelas = preco / qtde * 1.20
    precofinal = parcelas * qtde
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(qtde, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, precofinal))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')