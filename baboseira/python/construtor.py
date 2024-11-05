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