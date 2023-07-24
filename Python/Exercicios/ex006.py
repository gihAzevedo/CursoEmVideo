'''
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
'''

n = int(input("Digite um número: "))
db = n * 2
tp = n * 3
rq = n ** (1/2)

print('='*60)
print('O numero digitado foi: {} \n O dobro é: {} \n O triplo: {} \n A raiz Quadrada: {:.2f} '.format(n, db, tp, rq))
