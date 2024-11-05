class Animal():
    def __init__(self, nome, idade, nomeTutor, porte):
        self.nome = nome.capitalize()
        self.idade = idade
        self.nomeTutor = nomeTutor.capitalize()
        self.porte = porte.capitalize()
    def comunicacao(self):
        print("Sou um animal. Portanto, faço barulho.")
    def comportamento(self):
        print("Essa é minha forma de agir.")

class Cachorro(Animal):
    def comunicacao(self):
        print(f"Meu dono é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de latir e de brincar com meu/minha dono(a) {self.nomeTutor}.")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu/minha {self.nomeTutor}.")

class Passaro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu/minha dono(a) é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu/minha dono(a) {self.nomeTutor}.")

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

c = AnimalFactory.criarAnimal("Cachorro", "Bebeto", 8, "Marcelo", "Pequeno")
c.comunicacao()
c.comportamento()

g = AnimalFactory.criarAnimal("gato", "Bolinha", 7, "Tifa", "Pequeno")
g.comunicacao()
g.comportamento()

p = AnimalFactory.criarAnimal("passaro", "Juninho", 10, "Denise", "Médio")
p.comunicacao()
p.comportamento()