'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1250,00. Calcule um aumento de 10%.
- Para salários inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite o seu salário: R$'))
if salario <= 1250:
  novo = salario * 1.15
else:
    novo = salario * 1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))