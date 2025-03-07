class Animal():
    def __init__(self, nome, idade, nomeTutor, porte):
        self.nome = nome
        self.idade = idade
        self.nomeTutor = nomeTutor
        self.porte = porte
    def comunicacao(self):
        print("Sou um animal, portanto, faço barulho.")
    def comportamento(self):
        print("Essa é minha forma de agir.")

class Cachorro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosoto de latir e de brincar com meu dono {self.nomeTutor}.")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir e de deixar meu dono {self.nomeTutor} no vácuo.")

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

cachorro = AnimalFactory.criarAnimal("cachorro", "Luca", 4, "Paulo", "Médio")
cachorro.comunicacao()
cachorro.comportamento()

gato = AnimalFactory.criarAnimal("gato", "Nino", 10, "Fernando", "Pequeno")
gato.comunicacao()
gato.comportamento()

passaro = AnimalFactory.criarAnimal("passaro", "Gigi", 16, "Nathan", "Médio")
passaro.comunicacao()
passaro.comportamento()