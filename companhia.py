class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def bonificacao(self):
        bonificacao = self.salario * 0.1
        print(f"Bonificação: {bonificacao} \n")

