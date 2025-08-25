from historico import Historico

class Conta():
    def __init__(self,  numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(numero, cliente)

    def sacar(self, valor: float):

        if valor > self._saldo:
            print("Operação falhou! Você não possui saldo suficiente")

        elif valor > 0:
            self._saldo -= valor
            print("O saldo foi realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! O valor enviado não é válido")

    def depositar(self, valor: float):
        if valor > 0: 
            self._saldo += valor
            print("O depósito de R$ {valor} foi realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor enviado não é válido")



class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, Cliente, Historico, limite: float, limite_saques: int):
        super().__init__(saldo, numero, agencia, Cliente, Historico)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """