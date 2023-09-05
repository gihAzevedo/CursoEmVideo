valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())


#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

while periodo > 0:
    valor_inicial+= (valor_inicial*taxa_juros)
    periodo-=1
print(f"Valor final do investimento: R${valor_inicial:.2f}")