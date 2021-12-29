from abc import ABC,abstractmethod

class Animal(ABC):
    def correr(self):
        print("correr")

    @abstractmethod
    def respirar(self):
        pass

class Cao(Animal):
    def respirar(self):
        print("respirar como um cao")

class Passaro(Animal):

    def respirar(self):
        print("respirar como um passaro")

cao =Cao()
passaro = Passaro()
cao.correr()
cao.respirar()
