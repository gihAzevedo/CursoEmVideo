saldo = 0.0
while True:
    try:
        valor = float(input("Digite o valor do depósito (ou 0 para sair): "))
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            if valor == 0:
                print("Encerrando o programa...")
                break
            else:
                print("Valor inválido! Digite um valor maior que zero.")
    except ValueError:
        print("Valor inválido! Digite um valor numérico.")