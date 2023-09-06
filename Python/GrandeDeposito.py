saldo = 0
valor = float(input())
if valor > 0:
    saldo+= valor
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
elif valor == 0:
   print("Encerrando o programa...")
else:
    while valor < 0:
        print("Valor invalido! Digite um valor maior que zero.")
        valor = float(input())
        if valor > 0:
            saldo += valor
            print("Deposito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
            break
        elif valor == 0:
            print("Encerrando o programa...")
            break
