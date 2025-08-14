class RedePetriBanco:
    def __init__(self, saldoInicial = 0.0):
        self.saldo = saldoInicial
        self.places = {
            "Saldo": saldoInicial,
            "Depósito": 0,
            "Saque": 0,
            "Consulta": 0
        }

    def depositar(self, valor = 0.0):
        self.places['Depósito'] += valor
        self.places['Saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.places['Saldo']:.2f} \n")
    
    def sacar(self, valor = 0.0):
        if self.places['Saldo'] >= valor:
            self.places['Saque'] += valor
            self.places['Saldo'] -= valor
            print(f"Sauqe de R$ {valor:.2f} realizado. Saldo atual: R$ {self.places['Saldo']:.2f} \n")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        self.places['Consulta'] += 1
        print(f"Saldo atual: R$ {self.places['Saldo']:.2f} \n")
    
    def definir_saldo_inicial(self):
        valor = float(input("Informe o saldo inicial: "))
        self.saldo = valor
        self.places['Saldo'] = valor
        print(f"Saldo inicial definido como R$ {self.saldo:.2f}")

    def menu(self):
        operando = True
        while operando:
            print("Caixa Eletrônico")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Consultar Saldo")
            print("4. Sair")
            operacao = input("Informe a operação a ser realizada: ")
            match(operacao):
                case '1':
                    valor = float(input("Informe o valor a ser depositado: "))
                    self.depositar(valor)
                case '2':
                    valor = float(input("Informe o valor a ser sacado: "))
                    self.sacar(valor)
                case '3':
                    self.consultar_saldo()
                case '4':
                    print("Saindo...")
                    operando = False
                    break
                case _:
                    print("Operação inválida. Tente novamente.")

banco = RedePetriBanco()
banco.definir_saldo_inicial()
banco.menu()