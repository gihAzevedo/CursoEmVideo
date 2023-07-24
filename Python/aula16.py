print('{:-^65}'.format(' AULA DE TUPLAS '))
print('\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # vai juntar as duas tuplas
print(c)
print(len(c)) # mostra o tamanho da tupla
print(c.count(5)) # vai mostrar quantas vezes aparece o número 5 na Tupla
print(c.index(8)) # Mostra em que posição está o número 8
print(c.index(5, 2)) # vai mostrar o numero 5 a partir da segunda  posição(deslocamento)

'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche)) # Ordena a Tupla, mas não altera a posição


for comida in lanche:
    print(f'Eu vou comer {comida}') # Se não precisar da posição
print('='*40)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#vai mostrar todos os elementos da tupla com a posição
print('='*40)
for pos, comida in enumerate(lanche):
    print(f'EU vou comer {comida} na posição {pos}') # igual o segundo
print('='*40)
print('Comi pra caramba!')


print(lanche) # vai mostrar tudo
print(lanche[1])# vai mostrar apenas o primeiro elemento no caso: 'Suco'
print(lanche[-2]) # vai mostrar o segundo elemento da direita para esquerda: 'Pizza'
print(lanche[1:3])# Vai mostrar a partir do primeiro elemento ignorando o Terceiro elemento no caso: 'Pudim'
print(lanche[2:])# Vai mostrar do elemento 2 para frente.
print(lanche[:2])# vai mostrar os primeiros elementos parando no 2(não mostrando).

print(len(lanche)) # mostra o tamanho da tupla
'''