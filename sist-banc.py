menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> 
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação inválida")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não autorizada, saldo insuficiente.")

        elif excedeu_limite:
            print("Transação não autorizada, limite de saque quinhentos reais.")

        elif excedeu_saques:
            print("Limite diário de três saques")

    
        elif valor > 0:
            saldo -= valor

            extrato += f"Saque: R$ {valor:.2f}\n"

            numero_saques += 1

        else:
            print("Operação falhou, valor inválido.")

    elif opcao == "e":
        print("\n******************* EXTRATO ***********************")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**************************************************")

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, digite uma opção")



