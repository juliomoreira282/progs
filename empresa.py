class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def bonificacao(self):
        bonificacao = self.salario * 0.1
        print(f"Bonificação: {bonificacao} \n")

class Gerente(Funcionario):
    def __init__(self, nome, salario, usuario, senha):
        super().__init__(nome, salario)
        self.usuario = usuario
        self.senha = senha
    def bonificacao(self):
        bonificacao = self.salario * 0.6 + 100
        print(f"Bonificação: {bonificacao} \n")
    
class Secretaria(Funcionario):
    def __init__(self, nome, salario, ramal):
        super().__init__(nome, salario)
        self.ramal = ramal

class Telefonista(Funcionario):
    def __init__(self, nome, salario, estacaoDeTrabalho):
        super().__init__(nome, salario)
        self.estacaoDeTrabalho = estacaoDeTrabalho

funcionario = Funcionario("Silvio", 1800.0)
print(f"Nome: {funcionario.nome}")
print(f"Salário: {funcionario.salario}")
funcionario.bonificacao()

gerente = Gerente("Fabio", 10000.0, "fabinho", "fabinho123")
print(f"Nome: {gerente.nome}")
print(f"Salário: {gerente.salario}")
print(f"Usuário: {gerente.usuario}")
print(f"Senha: {gerente.senha}")
gerente.bonificacao()

secretaria = Secretaria("Beatriz", 2000.0, 16)
print(f"Nome: {secretaria.nome}")
print(f"Salário: {secretaria.salario}")
print(f"Ramal: {secretaria.ramal}")
secretaria.bonificacao()

telefonista = Telefonista("Viviane", 1750.0, "Centro")
print(f"Nome: {telefonista.nome}")
print(f"Salário: {telefonista.salario}")
print(f"Estação de Trabalho: {telefonista.estacaoDeTrabalho}")
telefonista.bonificacao()