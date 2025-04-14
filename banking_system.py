# Banking System DOCUMENTATION
# This program is a simple banking system designed as part of SUZANO-DIO Python Bootcamp.
# Task consisted in making a simple banking system with the following parameters:
# 1 - User can deposit, withdraw or check balance;
# 2 - there is a limit of maximum withdrawals (3);
# 3 - there is a limit to the maximum value of a single withdrawal (R$500);
# This program features an interactive menu for ease of use.

# Usage Instructions:
# Run the program and select your choices to deposit, withdraw and check account balance.

# Features:
# - **Deposit Funds:** Add money to your account.
# - **Withdraw Funds:** Withdraw cash with per-transaction and daily limits.
# - **Check Balance:** View your current balance and transaction history.
# - **Withdrawal Limits:** Maximum of 3 withdrawals per session and R$500 per transaction.

#  Notes:
# - Follow the on-screen prompts in this CLI-based menu that loops until the user chooses to quit.
# - System messages are in Portuguese (PT-BR) as per task instructions.

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

    if choice == "d":
        try:
            value = float(input("Informe o valor do depósito: "))

        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
            continue

        if value > 0:
            balance += value
            statement += f"Depósito: R$ {value:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif choice == "w":
        try:
            value = float(input("Informe o valor do saque: "))

        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
            continue

        overdraft = value > balance

        over_limit = value > limit

        over_withdraw = num_withdraw >= MAX_WITHDRAW

        if overdraft:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif over_limit:
            print("Operação falhou! O valor do saque excede o limite.")

        elif over_withdraw:
            print("Operação falhou! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            statement += f"Saque: R$ {value:.2f}\n"
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
