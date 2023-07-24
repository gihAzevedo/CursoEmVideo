galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')




'''  
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 7]]

for p in galera:
   # print(p) Mostra todos os elementos um embaixo do outro
   # print(p[0])  MOstra todos os nomes
   print(f'{p[0]} tem {p[1]} anos de idade.') # Print formatado
 
print(galera) # Mostra lista completa
print(galera[0]) # Mostra apenas o elemento 0: João, 19
print(galera[0][0]) # Mostra apenas o elemento 0 do indice 0: João
print(galera[2][1]) # Mostra apenas o elemento 1 do indice 2: 13
'''
'''
teste = list()
teste.append('Gideane')
teste.append(24)
galera = list()
galera.append(teste[:]) # NÃO ESQUECER QUE OS ":" DENTRO DOS COLCHETES SERVEM PARA COPIAR A LISTA, SEM ELES A LISTA POSSUIRIA UMA LIGAÇÃO DIRETA.
teste[0] = 'Maria Luiza'
teste[1] = 7
galera.append(teste[:])
print(galera)
'''