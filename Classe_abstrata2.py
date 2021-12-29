from abc import ABC,abstractmethod
from sys import exit
class Conta(ABC):

    def __init__(self,conta,saldo):
        self._conta = conta
        self._saldo = saldo

    @property
    def saldo(self):
       return self._saldo

    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    def depositar(self,valor):
            self._saldo +=valor

    @abstractmethod
    def sacar(self,valor):
        pass

class Conta_Poupanca(Conta):

    def __init__(self,conta,saldo):
        super().__init__(conta,saldo)

    def sacar(self,valor):
        limite = 400
        if valor <= limite:
            self._saldo -= valor
        else:
            print("O valor foi excedido")
            exit(0)

class Conta_Corrente(Conta):
    def __init__(self,conta,saldo):
        super().__init__(conta,saldo)

    def sacar(self,valor):
        limite = 600
        if valor <= limite:
            self._saldo -= valor
        else:
            print("O valor foi excedido")
            exit(0)

conta_poupanca = Conta_Poupanca(15046,500)
conta_poupanca.sacar(450)
print(conta_poupanca.saldo)


#conta = Conta(19032,400)
#conta.depositar(10)
#print(conta.saldo)
