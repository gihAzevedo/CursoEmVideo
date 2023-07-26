def area(largura, comprimento):
    resul = largura * comprimento
    print(f'A área de um terreno {largura:.1f} X {comprimento:.1f} é de {resul:.1f}m².')


print('Controle de Terrenos'.center(22))
print('-' * 22)
larg = float(input('LARGURA(m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)
