class AutomatoMatricula:
    def __init__(self):
        self.estado = 'Solicitação'
    
    def transicao(self, evento):
        if self.estado == 'Solicitação':
            if evento == 'Verificar':
                self.estado = 'Documentos Verificados'
                print("Documentos Verificados.")
            else:
                print("Aguardando verificação dos documentos.")
        
        elif self.estado == 'Documentos Verificados':
            if evento == 'Pagar':
                self.estado = 'Taxa Paga'
                print("Taxa paga.")
            else:
                print("Aguardando pagamento de taxa.")
        
        elif self.estado == 'Taxa Paga':
            if evento == 'Cadastrar':
                self.estado = 'Cadastro Realizado'
                print("Aluno cadastrado.")
            else:
                print("Aguardando cadastro.")
        
        elif self.estado == 'Cadastro Realizado':
            if evento == 'Finalizar':
                self.estado = 'Matrícula Concluída'
                print("Matrícula concluída.")
            else:
                print("Aguardando finalização.")

        elif self.estado == 'Matrícula Concluída':
            print("Matrícula já realizada.")
        
        else:
            print("Estado desconhecido.")
        
        self.mostrar_estado()

    def solicitar_matricula(self):
        print("Solicitação de matrícula recebida.")
        self.mostrar_estado()
    
    def mostrar_estado(self):
        print(f"Estado atual: {self.estado}")
        print("-" * 30)

automato = AutomatoMatricula()
automato.solicitar_matricula()

while True:
    evento = input("Evento: ").capitalize()
    if evento.lower() == 'sair':
        print("Encerrando...")
        break

    automato.transicao(evento)