from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def comunicacao(self):
        pass
    def comportamento(self):
        pass

class Cachorro(Animal):
    def comunicacao(self):
        print("Au au.")
    def comportamento(self):
        print("Brincar e latir.")

class Gato(Animal):
    def comunicacao(self):
        print("Miau.")
    def comportamento(self):
        print("Dormir e miar.")

class Passaro(Animal):
    def comunicacao(self):
        print("Piu piu.")
    def comportamento(self):
        print("Cantar e voar.")

animal = Cachorro()
animal2 = Gato()
animal3 = Passaro()
animal.comunicacao()
animal.comportamento()
animal2.comunicacao()
animal2.comportamento()
animal3.comunicacao()
animal3.comportamento()