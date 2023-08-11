menu = """
--===========Menu===========--

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Selecione uma operação: """

LIMITE_SAQUES = 3
numero_saque = 0
numero_deposito = 0
limite = 500
deposito = 0
saldo = 0
saque = ""
extrato = ""

while True:
    opção = input(menu)

    if opção == "d":

        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor 
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        else:
            print("Falha na operação, valor informado é inválido. Tente novamente.")
        
    elif opção == "s":
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        if excedeu_saques:
            print("Número de saques excedido. Tente novamente.")
        elif excedeu_limite: 
            print("Limite insuficiente. Tente novamente.")
        elif valor > 0:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saque += 1
        else:
            print("Operação inválida. Tente novamente.")

    elif opção == "e":
        print("\n--===========EXTRATO===========--")
        print("Não foram realizada movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--=============================--")

    elif opção == "q":
        print("Finalizando.")
        break

    else:
        print("Operação inválida. Tente novamente")
