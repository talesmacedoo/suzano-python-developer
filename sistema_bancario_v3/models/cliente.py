
class Cliente():
    def __init__(self, endereco: SyntaxWarning):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf: str, nome: str, data_nascimento: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome