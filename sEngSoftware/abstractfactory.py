from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade, nomeTutor, porte):
        self.nome = nome
        self.idade = idade
        self.nomeTutor = nomeTutor
        self.porte = porte
    @abstractmethod
    def comunicacao(self):
        pass
    @abstractmethod
    def comportamento(self):
        pass

class Cachorro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de latir e de brincar com meu dono {self.nomeTutor}.")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu dono {self.nomeTutor}.")

class Passaro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu nome é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu dono {self.nomeTutor}.")

class AnimalFactory(ABC):
    @abstractmethod
    def criarAnimal(self, nome, idade, nomeTutor, porte) -> Animal:
        pass

class FabricaCachorro(AnimalFactory):
    def criarAnimal(self, nome, idade, nomeTutor, porte):
        return Cachorro(nome, idade, nomeTutor, porte)

class FabricaGato(AnimalFactory):
    def criarAnimal(self, nome, idade, nomeTutor, porte):
        return Gato(nome, idade, nomeTutor, porte)

class FabricaPassaro(AnimalFactory):
    def criarAnimal(self, nome, idade, nomeTutor, porte):
        return Passaro(nome, idade, nomeTutor, porte)
    
def criarExibirAnimal(factory: AnimalFactory, nome, idade, nomeTutor, porte):
    animal = factory.criarAnimal(nome, idade, nomeTutor, porte)
    animal.comunicacao()
    animal.comportamento()

criarExibirAnimal(FabricaCachorro(), "Fred", 5, "Victor", "Médio")
criarExibirAnimal(FabricaGato(), "Cecília", 3, "Gabriela", "Pequeno")
criarExibirAnimal(FabricaPassaro(), "Zezé", 12, "Fabio", "Médio")