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
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cachorro, cls).__new__(cls)
        return cls._instance
    def __init__(self, nome, idade, porte, nomeTutor):
        if not hasattr(self, '_initialized'):
            super().__init__(nome, idade, nomeTutor, porte)
            self._initialized = True
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de latir e de brincar com meu dono {self.nomeTutor}.")

class Gato(Animal):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cachorro, cls).__new__(cls)
        return cls._instance
    def __init__(self, nome, idade, porte, nomeTutor):
        if not hasattr(self, '_initialized'):
            super().__init__(nome, idade, nomeTutor, porte)
            self._initialized = True
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto de dormir e de ignorar meu dono {self.nomeTutor}.")

class Passaro(Animal):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cachorro, cls).__new__(cls)
        return cls._instance
    def __init__(self, nome, idade, porte, nomeTutor):
        if not hasattr(self, '_initialized'):
            super().__init__(nome, idade, nomeTutor, porte)
            self._initialized = True
    def comunicacao(self):
        print(f"Meu nome é {self.nome} e meu dono é {self.nomeTutor}.")
    def comportamento(self):
        print(f"Gosto muito de cantar para meu dono {self.nomeTutor}.")

c1 = Cachorro("Fred", 5, "Victor", "Médio")
c2 = Cachorro("Charles", 8, "Jaime", "Grande")
print(c1 is c2)
c1.comunicacao()
c2.comunicacao()
c1.comportamento()
c2.comportamento()

g1 = Gato("Cecília", 3, "Gabriela", "Pequeno")
g2 = Gato("Sophia", 14, "Natasha", "Médio")
print(g1 is g2)
g1.comunicacao()
g2.comunicacao()
g1.comportamento()
g2.comportamento()

p1 = Passaro("Zezé", 12, "Fabio", "Médio")
p2 = Passaro("Marcelo", 16, "Fernanda", "Pequeno")
print(p1 is p2)
p1.comunicacao()
p2.comunicacao()
p1.comportamento()
p2.comportamento()