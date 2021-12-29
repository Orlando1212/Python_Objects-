class Conta:
    def __init__(self,nome,saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor


conta = Conta("Orlando",300)
conta.depositar(100)
print(conta.saldo)