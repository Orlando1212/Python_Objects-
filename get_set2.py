class Conta:
    def __init__(self,saldo):
        self._numero = 0
        self._saldo = saldo
                                    #@propety
    def get_numero(self):           #def numero(self)
        return self._numero
                                    #@numero.setter
    def set_numero(self,valor):     #def numero(self,valor)
        if valor > 0:
            self._numero = valor
        else:
            print("numero invalido")

    def depositar(self,valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor


conta = Conta(300)
conta.set_numero(14562)         #conta.numero = 14562
print(conta.get_numero())       #print(conta.numero)