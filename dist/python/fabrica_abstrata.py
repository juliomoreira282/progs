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
        print(f"Meu nome é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de latir e de brincar com meu/minha dono(a) {self.nomeTutor}.")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu/minha dono(a) {self.nomeTutor}.")

class Passaro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu/minha dono(a) {self.nomeTutor}.")

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

criarExibirAnimal(FabricaCachorro(), "Bebeto", 8, "Marcelo", "Pequeno")
criarExibirAnimal(FabricaGato(), "Bolinha", 7, "Tifa", "Pequeno")
criarExibirAnimal(FabricaPassaro(), "Juninho", 10, "Denise", "Médio")