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
            print("Deposito realizado com sucesso!")
        else: 
            print("Valor digitado é menor ou igual a zero")

    elif opcao == "s":
        pass

    elif opcao == "e":
        print("\n================ EXTRATO ================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")