class PetriNet:
    def __init__(self):
        self.places = {
            'Solicitação': 0,
            'Documentos Verificados': 0,
            'Taxa Paga': 0,
            'Cadastro Realizado': 0,
            'Matrícula Concluída': 0
        }
    
    def adicionar_matriculas(self, quantidade):
        self.places['Solicitação'] += quantidade
        print(f"{quantidade} solicitações de matrícula pendentes.")
        self.estado_atual()

    def verificar_documentos(self):
        while self.places['Solicitação'] > 0:
            if self.places['Solicitação'] > 0:
                self.places['Solicitação'] -= 1
                self.places['Documentos Verificados'] += 1
                print("Documentos verificados.")
                self.estado_atual()
            else:
                print("Nenhuma solicitação de matrícula pendente.")
    
    def pagar_taxa(self):
        while self.places['Documentos Verificados'] > 0:
            if self.places['Documentos Verificados'] > 0:
                self.places['Documentos Verificados'] -= 1
                self.places['Taxa Paga'] += 1
                print("Taxa paga.")
                self.estado_atual()
            else:
                print("Documentos não foram verificados.")
    
    def realizar_cadastro(self):
        while self.places['Taxa Paga'] > 0:
            if self.places['Taxa Paga'] > 0:
                self.places['Taxa Paga'] -= 1
                self.places['Cadastro Realizado'] += 1
                print("Cadastro realizado.")
                self.estado_atual()
            else:
                print("A taxa ainda não foi paga.")
    
    def concluir_matricula(self):
        while self.places['Cadastro Realizado'] > 0:
            if self.places['Cadastro Realizado'] > 0:
                self.places['Cadastro Realizado'] -= 1
                self.places['Matrícula Concluída'] += 1
                print("Matrícula concluída.")
                self.estado_atual()
            else:
                print("O cadastro ainda não foi realizado.")
            
    def estado_atual(self):
        print("Estado atual:")
        for place, quantidade in self.places.items():
            print(f"{place}: {quantidade}")
        print("-" * 30)

rede = PetriNet()
rede.adicionar_matriculas(1)
rede.verificar_documentos()
rede.pagar_taxa()
rede.realizar_cadastro()
rede.concluir_matricula()