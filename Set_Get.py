class Filtro:

    def __init__(self,imagem):
        self.imagem = imagem

    def preto_branco(self):
        print(f'{self.imagem} foi preto e branco')

    def envelhecida(self):
        print(f'{self.imagem} foi envelhecida')


filtro = Filtro('Foto do Doctor')
filtro.preto_branco()