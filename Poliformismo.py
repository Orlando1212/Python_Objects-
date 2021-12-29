class Animal:
    def __init__(self,cor,tamanho,peso):
        self.cor  = cor
        self.tamanho = tamanho
        self.peso = peso

    def correr(self):
        print("correr como um")

    def dormir(self):
        print("dormir")

class Cao(Animal):
    def __init__(self,cor,tamanho,peso):
        super().__init__(cor,tamanho,peso)

    def latir(self):
        print("latir")

    def correr(self):
        super().correr()
        print('cao')

class Passaro(Animal):
    def __init__(self,cor,tamanho,peso):
        super().__init__(cor,tamanho,peso)

    def voar(self):
        print("voar")

    def correr(self):
        super().correr()
        print('passaro')

cao = Cao('Marrom','30cm','5kg')
passaro = Passaro('Amarelo','10cm','500g')
#cao.correr()
