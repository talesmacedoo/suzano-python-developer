
class Cliente():
    def __init__(self, endereco: str, contas: list):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):

        #implementar lógica de transação
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        #implementar lógica de adicionar contas
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf: str, nome: str, data_nascimento: str):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento