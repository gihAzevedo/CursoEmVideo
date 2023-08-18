def moeda(preco=0, moeda='R$'):
 return f'{moeda}{preco:.2f}'.replace('.', ',')

def metade(preco, formatado = False):
    res = preco / 2
    return res if formatado is False else moeda(res)
def dobro(preco, formatado = False):
    res = preco * 2
    return res if formatado is False else moeda(res)
def aumentar(preco, porcentagem, formatado = False):
    res = preco + (preco * porcentagem / 100)
    return res if formatado is False else moeda(res)
def diminuir(preco, porcentagem, formatado = False):
    res = preco - (preco * porcentagem/ 100)
    return res if formatado is False else moeda(res)
