from datetime import datetime

class Reserva():
    def __init__(self, check_in, check_out, tipo_quarto, num_pessoas, nome_hospede):
        self.check_in = check_in
        self.check_out = check_out
        self.tipo_quarto = tipo_quarto
        self.num_pessoas = num_pessoas
        self.nome_hospede = nome_hospede
        self.status = "Confirmada"

class Funcionario():
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Chatbot():
    def __init__(self):
        self.reservas = []
        self.funcionarios = {}
    def iniciar_conversa(self):
        print("Seja bem-vindo à nossa pousada em Maceió!")
        while True:
            print("Como posso ajudar?")
            print("1. Fazer uma reserva.")
            print("2. Informações Turísticas.")
            print("3. FAQs.")
            print("4. Gerenciar funcionários.")
            print("5. Login para funcionários.")
            print("6. Sair.")
            escolha = int(input("Escolha uma opção: (1, 2, 3, 4, 5, 6)."))
            match(escolha):
                case 1:
                    self.manipular_reserva()
                case 2:
                    self.fornecer_info_turistica()
                case 3:
                    self.responder_faqs()
                case 4:
                    self.gerenciar_funcionarios()
                case 5:
                    self.login_admin()
                case 6:
                    print("Obrigado por visitar nossa pousada. Até a próxima!")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
    def gerenciar_funcionarios(self):
        print("Gerenciar Funcionários:")
        while True:
            print("O que gostaria de fazer?")
            print("1. Adicionar funcionário:")
            print("2. Listar funcionário:")
            print("3. Voltar:")
            escolha = int(input("Escolha uma opção: (1, 2, 3)."))
            match(escolha):
                case 1:
                    self.adicionar_funcionario()
                case 2:
                    self.listar_funcionario()
                case 3:
                    return
                case _:
                    print("Opção inválida. Tente novamente.")
    def adicionar_funcionario(self):
        usuario = input("Nome: ")
        senha = input("Senha: ")
        if usuario in self.funcionarios:
            print("Esse usuário já existe. Tente novamente.")
        else:
            self.funcionarios[usuario] = Funcionario(usuario, senha)
            print("Usuário adicionado com sucesso!")
    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Não há funcionários cadastrados.")
            return
        print("Usuários cadastrados: ")
        for usuario in self.funcionarios:
            print(f"- {usuario}")
    def login_admin(self):
        print("Área de login para funcionários:")
        usuario = input("Nome: ")
        senha = input("Senha: ")
        if usuario in self.funcionarios and self.funcionarios[usuario].senha == senha:
            print("Login bem-sucedido!")
        else:
            print("Credenciais inválidas. Tente novamente.")
    def mostrar_informacoes_hospedes(self):
        if not self.reservas:
            print("Não há reservas ativas no momento.")
            return
        print("Informações dos Hóspedes:")
        for i, reserva in enumerate(self.reservas, start=1):
            print(f"{i}. Nome do Hóspede: {reserva.nome_hospede}, {reserva.num_pessoas}, pessoa(s) - {reserva.tipo_quarto} de {reserva.check_in} a {reserva.check_out}")
    def validar_data(self, data_texto):
        try:
            return datetime.strptime(data_texto, "%D/%M/%Y")
        except ValueError:
            print("Data Inválida. Tente novamente no formato DD/MM/AAAA.")
            return None
    def manipular_reserva(self):
        print("Vamos começar a reserva.")
        nome_hospede = input("Nome do hóspede: ")
        while True:
            check_in = input("Data de Check-In (DD/MM/AAAA)")
            check_in_data = self.validar_data(check_in)