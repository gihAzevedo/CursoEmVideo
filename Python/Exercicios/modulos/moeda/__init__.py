def metade(preco):
    m = preco / 2
    return m
def dobro(preco):
    d = preco * 2
    return d
def aumentar(preco, porcentagem):
    a = preco + (preco * porcentagem / 100)
    return a
def diminuir(preco, porcentagem):
    r = preco - (preco * porcentagem/ 100)
    return r

def moeda(preco):
    conversao = str(f'R${preco:.2f}')
    conversao = conversao.replace('.', ',')
    return conversao