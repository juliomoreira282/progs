class Animal():
    def comunicacao(self):
        print("Sou um animal, portanto, faço barulho.")
    def comportamento(self):
        print("Essa é minha forma de agir.")

class Cachorro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}")
    def comportamento(self):
        print(f"Gosto delatir e de brincar com meu dono {self.nomeTutor}")

class Gato(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu dono {self.nomeTutor}")

class Passaro(Animal):
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu dono {self.nomeTutor}.")

class AnimalFactory():
    @staticmethod
    def criaranimal(tipo, nome, idade, nomeTutor, porte):
        match(tipo.capitalize()):
            case "Cachorro":
                return Cachorro(nome, idade, nomeTutor, porte)
            case "Gato":
                return Gato(nome, idade, nomeTutor, porte)
            case "Passaro":
                return Passaro(nome, idade, nomeTutor, porte)
            case _:
                return None


c = AnimalFactory.criaranimal("cachorro", "Fred", 5, "Victor", "Médio")
c.comunicacao()
c.comportamento()

g = AnimalFactory.criaranimal("gato", "Cecília", 3, "Gabriela", "Pequeno")
g.comunicacao()
g.comportamento()

p = AnimalFactory.criaranimal("passaro", "Zezé", 12, "Fabio", "Médio")
p.comunicacao()
p.comportamento()