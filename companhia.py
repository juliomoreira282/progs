class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def bonificacao(self):
        bonificacao = self.salario * 0.1
        print(f"Bonificação: {bonificacao} \n")

class Gerente(Funcionario):
    def __init__(self, nome, salario, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        super().__init__(nome, salario)
    def bonificacao(self):
        bonificacao = self.salario * 0.6 + 100
        print(f"Bonificação: {bonificacao} \n")

class Secretaria(Funcionario):
    def __init__(self, nome, salario, ramal):
        self.ramal = ramal
        super().__init__(nome, salario)
    def bonificacao(self):
        bonificacao = self.salario * 0.3 + 50
        print(f"Bonificação: {bonificacao} \n")

class Telefonista(Funcionario):
    def __init__(self, nome, salario, estacaoDeTrabalho):
        self.estacaoDeTrabalho = estacaoDeTrabalho
        super().__init__(nome, salario)
    def bonificacao(self):
        bonificacao = self.salario * 0.2 + 25
        print(f"Bonificação: {bonificacao} \n")

funcionario = Funcionario("Kevin", 1500.0)
print(f"Nome: {funcionario.nome}")
print(f"Salário: {funcionario.salario}")
funcionario.bonificacao()

gerente = Gerente("Carlos", 7850.0, "carletto", "carlos66484")
print(f"Nome: {gerente.nome}")
print(f"Salário: {gerente.salario}")
print(f"Usuário: {gerente.usuario}")
print(f"Senha: {gerente.senha}")
gerente.bonificacao()

secretaria = Secretaria("Vitória", 3500.0, 24)
print(f"Nome: {secretaria.nome}")
print(f"Salário: {secretaria.salario}")
print(f"Ramal: {secretaria.ramal}")
secretaria.bonificacao()

telefonista = Telefonista("Juliana", 2000.0, "Centro")
print(f"Nome: {telefonista.nome}")
print(f"Salário: {telefonista.salario}")
print(f"Estação de Trabalho: {telefonista.estacaoDeTrabalho}")
telefonista.bonificacao()