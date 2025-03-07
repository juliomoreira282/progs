class Animal():
    def __init__(self, nome, idade, nomeTutor, porte):
        self.nome = nome.capitalize()
        self.idade = idade
        self.nomeTutor = nomeTutor.capitalize()
        self.porte = porte.capitalize()    
    def comunicacao(self):
        print("Sou um animal, portanto, faço barulho.")
    def comportamento(self):
        print("Essa é minha forma de agir.")

class Cachorro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de latir e de brincar com meu dono {self.nomeTutor}.")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir, ignorar e de pedir comida ao meu dono {self.nomeTutor}.")

class Passaro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu dono {self.nomeTutor}.")

class AnimalFactory():
    @staticmethod
    def criarAnimal(tipo, nome, idade, nomeTutor, porte):
        match(tipo.capitalize()):
            case "Cachorro":
                return Cachorro(nome, idade, nomeTutor, porte)
            case "Gato":
                return Gato(nome, idade, nomeTutor, porte)
            case "Passaro":
                return Passaro(nome, idade, nomeTutor, porte)
            case _:
                return None

cachorro = AnimalFactory.criarAnimal("cachorro", "Plínio", 5, "Marco", "Grande")
cachorro.comunicacao()
cachorro.comportamento()

gato = AnimalFactory.criarAnimal("gato", "Jujuba", 3, "Larissa", "Pequeno")
gato.comunicacao()
gato.comportamento()

passaro = AnimalFactory.criarAnimal("passaro", "Zezé", 12, "Eduardo", "Médio")
passaro.comunicacao()
passaro.comportamento()