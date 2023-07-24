'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Corinthians.
'''
times = ('Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Fluminense', 'Athletico-PR', 'São Paulo',
           'Fortaleza', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Santos', 'Internacional', 'Cuiabá',
           'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco', 'Coritiba')
print('-=' * 15)
print(f'Lista de Times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Corinthians está na {times.index("Corinthians")+1} posição.')
print('-=' * 15)
