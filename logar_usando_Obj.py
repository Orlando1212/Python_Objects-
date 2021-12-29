from sys import exit
class Usuario:

    def __init__(self , email , senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'email: {self.email}, senha: {self.senha}'

    def Validar(self):
        email_c = 'doctorstrange@hotmail.com'
        senha_c = '12345'

        if email_c == self.email and senha_c == self.senha:
            print('Usuario Logado')
        else :
            print('Usuario Invalido')
            exit(0)


    def Logar(self):
        self.Validar()
        print("Bem vindo a tela principal")


    def Cadastra_Enderecos(self, *enderecos):
        for endereco in enderecos:
            print(f'endereco :{endereco}')

usuario = Usuario('doctorstrange@hotmail.com','12345')
lista = ['Rua Tibirica','Rua Major Novaes']
usuario.Cadastra_Enderecos(lista)
# usuario.Logar()
print(usuario)