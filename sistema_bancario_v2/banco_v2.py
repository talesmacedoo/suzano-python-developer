

def sacar(saldo:float, valor:float, extrato:str, limite:float, numero_saques:int, limite_saques ):
    ''''''
    return saldo, extrato

def depositar(saldo:float, valor:float, extrato:str):
    return saldo, extrato

def visualizar_historico(saldo,*,extrato:str):
    pass

def criar_usuario(nome:str, data_nascimento:str, cpf:str, endereco:str):
    pass

def criar_conta_corrente(numero_ultima_conta: int, usuario):
    agencia = "0001"
    pass

def main():

    while True:

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

        usuarios = []

        contas = []
        numero_ultima_conta = 0
        
        opcao = input(menu)




        if opcao == "d":
            pass
        elif opcao == "s":
            pass

        elif opcao == "e":
            pass
        elif opcao == "q":
            pass

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()