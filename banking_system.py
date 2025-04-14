menu = """

[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

MAX_WITHDRAW = 3
balance = 0
limit = 500
statement = ""
num_withdraw = 0


while True:
    choice = input(menu).strip().lower()

    if choice not in "dwsq":
        print("Opção inválida. Por favor, escolha uma das opções listadas.")

    if choice == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            balance += valor
            statement += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif choice == "w":
        valor = float(input("Informe o valor do saque: "))

        overdraft = valor > balance

        over_limit = valor > limit

        over_withdraw = num_withdraw >= MAX_WITHDRAW

        if overdraft:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif over_limit:
            print("Operação falhou! O valor do saque excede o limite.")

        elif over_withdraw:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            balance -= valor
            statement += f"Saque: R$ {valor:.2f}\n"
            num_withdraw += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif choice == "s":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not statement else statement)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif choice == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
