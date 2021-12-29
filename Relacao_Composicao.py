class Usuario:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []


    def insere_endereco(self,cep,cidade,rua):
        endereco = Endereco(cep,cidade,rua)
        self.enderecos.append(endereco)

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __del__(self):
        print(f'O {self.nome} foi apagado')

class Endereco:
    def __init__(self,cep,cidade,rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua


    def __str__(self):
        return f' cep {self.cep}, cidade {self.cidade}, rua {self.rua}'


    def __del__(self):
        print(f'A {self.rua} foi apagada')

usuario = Usuario("FredKrug21")
endereco = Endereco

usuario.insere_endereco("340532-20","canas-sp","Rua Tal")

usuario.lista_enderecos()