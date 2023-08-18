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

def resumo(preco=0, taxaA=10, taxaR=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'{taxaR}% de redução: \t{diminuir(preco, taxaR, True)}')
    print('-' * 30)

