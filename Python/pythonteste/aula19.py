# AULA DE DICIONÁRIOS
estado = dict()
brasil = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).upper().strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper().strip()[:2]
    brasil.append(estado.copy()) # Método para copiar dicionário para lista sem fazer uma ligação direta
print('-=' * 30)
for e in brasil: # Mostra cada estado da lista Brasil
    for v in e.values(): # Mostra os valores dos estados
        print(v, end=' ')
    print()
    '''
    for k, v in e.items(): # Mostra cada item de cada estado
        print(f'O campo {k} tem valor {v}.')
    print()
    '''

# print(brasil) - Mostra a lista

'''
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
# print(brasil[0]['uf']) - Mostra o UF(parâmetro) do primeiro elemento
# print(brasil[1]) -  mostra o primeiro elemento da lista.
# print(brasil) - mostra toda a lista com os dicionarios
'''

'''
pessoas = {'nome': 'Gideane', 'sexo': 'F', 'idade': 24}
pessoas['peso'] = 62.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 30)

print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos') # - Precisa ser aspas duplas
print(pessoas.keys()) # - Mostra as chaves
print(pessoas.values()) # - Mostra os valores
print(pessoas.items()) # - Mostra os itens
# print(pessoas['nome']) - Mostra o nome
# print(pessoas['idade']) - Mostra a idade
# print(pessoas['sexo']) - Mostra  o sexo
'''
