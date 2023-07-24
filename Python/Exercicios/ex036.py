'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
'''
imovel = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos pretende pagar o imóvel? '))
ano = ano *12
prestacao = imovel /(ano)
porcentagem = (prestacao*100)/salario
print('-=-'*40)
if prestacao <(salario*0.3):
    print('\033[1:32mEMPRÉSTIMO APROVADO!\033[m')
    print('O empréstimo possui \033[4:35m{}\033[m parcelas \nNo valor de \033[1:32mR${:.2f}\033[m cada.'.format(ano, prestacao))
    print('\033[4:34mO valor das parcelas irá consumir {:.2f}% do seu salário.'.format(porcentagem))
    print('\033[4:34mÉ possível realizar o empréstimo com uma quantidade menor de parcelas sem execeder 30% do seu salário.')
elif prestacao ==(salario*0.3):
    print('\033[1:32mEMPRÉSTIMO APROVADO!\033[m')
    print('O empréstimo possui \033[4:35m{}\033[m parcelas \nNo valor de \033[1:32mR${:.2f}\033[m cada.'.format(ano, prestacao))
    print('\033[4:34mO valor das parcelas irá consumir 30% do seu salário.\033[m')
    print('\033[1:31mNão é possível realizar uma nova simulação com uma quantidade inferior de parcelas')
else:
    print('\033[1:31mEMPRÉSTIMO REPROVADO!\033[m')
    print('O valor de cada uma das \033[4:31m{}\033[m parcelas ficaria em \033[1:31mR${:.2f}\033[m o que excederia 30% do seu salário.'.format(ano, prestacao))

