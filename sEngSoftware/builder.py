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

class AnimalBuilder():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.nomeTutor = None
        self.porte = None
        self.tipoAnimal = None
    def setNome(self, nome):
        self.nome = nome
        return self
    def setIdade(self, idade):
        self.idade = idade
        return self
    def setNomeTutor(self, nomeTutor):
        self.nomeTutor = nomeTutor
        return self
    def setPorte(self, porte):
        self.porte = porte
        return self
    def setTipoAnimal(self, tipoAnimal):
        self.tipoAnimal = tipoAnimal
        return self
    def build(self):
        match(self.tipoAnimal.capitalize()):
            case "Cachorro":
                return Cachorro(self.nome, self.idade, self.nomeTutor, self.porte)
            case "Gato":
                return Gato(self.nome, self.idade, self.nomeTutor, self.porte)
            case "Passaro":
                return Passaro(self.nome, self.idade, self.nomeTutor, self.porte)
            case _:
                raise ValueError("Tipo de animal inválido. Escolha entre 'Cachorro', 'Gato' ou 'Passaro'.")

builder = AnimalBuilder()
cachorro = (builder
    .setNome("Fred")
    .setIdade(5)
    .setNomeTutor("Victor")
    .setPorte("Médio")
    .setTipoAnimal("cachorro")
    .build())
cachorro.comunicacao()
cachorro.comportamento()

gato = (builder
    .setNome("Cecília")
    .setIdade(3)
    .setNomeTutor("Gabriela")
    .setPorte("Pequeno")
    .setTipoAnimal("gato")
    .build())
gato.comunicacao()
gato.comportamento()

passaro = (builder
    .setNome("Zezé")
    .setIdade(12)
    .setNomeTutor("Fabio")
    .setPorte("Médio")
    .setTipoAnimal("passaro")
    .build())
passaro.comunicacao()
passaro.comportamento()