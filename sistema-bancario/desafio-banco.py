menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do deposito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
        else: 
            print("Valor digitado é menor ou igual a zero")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor que você deseja sacar:"))
            if valor > 500:
                print("O valor de saque é de no máximo R$ 500,00")
            elif valor > saldo:
                print("O valor de saque é maior do que o saldo da conta")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque de: R$ {valor:.2f}\n"
                print(f"O saque de R$ {valor:.2f} foi realizado com sucesso!")
        else:
            print("Você já atingiu o número máximo de saques por dia.")        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"O saldo é de R$ {valor:.2f}")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")