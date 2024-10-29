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
    def __init__(self, nome, idade, nomeTutor, porte):
        Animal.__init__(self, nome, idade, nomeTutor, porte)
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}")
    def comportamento(self):
        print(f"Gosto delatir e de brincar com meu dono {self.nomeTutor}")

class Gato(Animal):
    def __init__(self, nome, idade, nomeTutor, porte):
        Animal.__init__(self, nome, idade, nomeTutor, porte)
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu dono {self.nomeTutor}")

class Passaro(Animal):
    def __init__(self, nome, idade, nomeTutor, porte):
        Animal.__init__(self, nome, idade, nomeTutor, porte)
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu dono {self.nomeTutor}.")

a = Animal("Igor", 10, "Carlos", "Grande")
a.comunicacao()
a.comportamento()

c = Cachorro("Fred", 5, "Victor", "Médio")
c.comunicacao()
c.comportamento()

g = Gato("Cecília", 3, "Gabriela", "Pequeno")
g.comunicacao()
g.comportamento()

p = Passaro("Zezé", 12, "Fabio", "Médio")
p.comunicacao()
p.comportamento()