def moeda(preco):
    conversao = str(f'R${preco:.2f}')
    conversao = conversao.replace('.', ',')
    return conversao


def metade(preco, formatado):
    m = preco / 2
    if formatado == True:
        m = moeda(m)
    return m
def dobro(preco, formatado):
    d = preco * 2
    if formatado == True:
        d = moeda(d)
    return d
def aumentar(preco, porcentagem, formatado):
    a = preco + (preco * porcentagem / 100)
    if formatado == True:
        a = moeda(a)
    return a
def diminuir(preco, porcentagem, formatado):
    r = preco - (preco * porcentagem/ 100)
    if formatado == True:
        r = moeda(r)
    return r
