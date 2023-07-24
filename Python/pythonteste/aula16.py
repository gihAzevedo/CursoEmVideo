'''
num = [2, 5, 9, 1]
num[2] = 3 # Troca o valor do elemento 2
num.append(7) # Adiciona um valor na lista o tornando o ultimo elemento.
num.sort() # Organiza a lista na ordem crescente
num.sort(reverse=True) # Organiza a lista na ordem decrescente
num.insert(2, 2) # adiciona no segundo elemento(começa no 0) o valor escolhido, no caso 0
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

# num.remove(2) # Procura do inicio da lista até a primeira ocorrência e o exclui.
# num.pop(2) # remove o último elemento, caso não passe nenhum elemento como parâmetro
print(num)
print(f'Essa lista tem {len(num)} elementos.') # Informa quantos elementos a lista possui começando pelo 1.
'''
'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)


for v in valores: #Mostra cada elemento da lista
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores): #Mostra a posição e o valor do elemento
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) # Adiciona um valor a lista direto pelo teclado através do comando For e Append.

for c, v in enumerate(valores): #Mostra a posição e o valor do elemento
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

'''
a = [2, 3, 4, 7]
# b = a # Ao identificar que a lista B é igual a lista A, é criada uma ligação entre elas e ao alterar um dos valores de qualquer uma das listas alterapara ambas
b = a[:] # Faz apenas uma cópia dos valores da lista A, não cria uma ligação entre elas permitindo assim que se altere os valores sem interferir na outra lista.
b[2] = 8
print(f'Lista A: {a}')
print(f'LIsta B: {b}')
'''