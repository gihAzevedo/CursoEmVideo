def metade(preco):
    m = preco / 2
    return m
def dobro(preco):
    d = preco * 2
    return d
def aumentar(preco, porcentagem=0):
    a = preco + (preco * porcentagem / 100)
    return a
def diminuir(preco, porcentagem=0):
    r = preco - (preco * porcentagem/ 100)
    return r

def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
