saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

def deposito(atual, deposito):
    resultado = atual + deposito
    return resultado

def saque(atual, retirada):
    resultado = atual - retirada
    return resultado



a = deposito(saldo_atual, valor_deposito)
b = saque(a, valor_retirada)
print(f"{b:.1f}")