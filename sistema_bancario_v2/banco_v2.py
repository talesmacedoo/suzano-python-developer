

def sacar(saldo:float, valor:float, extrato:str, limite:float, numero_saques:int, limite_saques: int):
    if numero_saques < limite_saques:
        if valor > limite:
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

    return saldo, extrato

def depositar(saldo:float, valor:float, extrato:str):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else: 
        print("Valor digitado é menor ou igual a zero")
    return saldo, extrato

def visualizar_historico(saldo: float,*,extrato: str):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"O saldo é de R$ {saldo:.2f}")

def criar_usuario(usuarios: list):
    cpf = input("Digite o CPF para criação da usuário: ")
    cpf = cpf.replace(".","").replace("-","")

    for usuario in usuarios:
        if usuario["Cpf"] == cpf:
            print("Já existe uma usuário cadastrado para esse CPF!")
            return usuarios
    nome = input("Digite o nome para criação da usuário: ")
    data_de_nascimento = input("Digite o data de nascimento para criação da usuário: ")
    endereco = input("Digite o endereço para criação da usuário: ")

    usuarios.append(
        {
        "nome": nome,
        "Cpf": cpf,
        "data de nascimento": data_de_nascimento,
        "endereco": endereco
        }
    )
    print(f"Usuário {nome} criado com sucesso!")

    return usuarios


def criar_conta_corrente(numero_ultima_conta: int, usuario):
    pass

def main():

    menu = """

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [q]  Sair
    [nu] Novo Usuário
    [cc] Criar Conta Corrente

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia = "0001"

    usuarios = []

    contas = []
    numero_ultima_conta = 0

    while True:       
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Digite o valor do deposito:"))
            saldo, extrato = depositar(saldo=saldo, valor= valor, extrato=extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor que você deseja sacar:"))
            saldo, extrato = sacar(saldo= saldo, valor= valor, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

        elif opcao == "e":
           visualizar_historico(saldo, extrato= extrato)

        elif opcao == "nu":
            usuarios = criar_usuario(usuarios= usuarios)
        elif opcao == "cc":
            pass
        elif opcao == "q":
            pass

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()