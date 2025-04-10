class Place:
    def __init__(self, name, tokens=0):
        self.name = name
        self.tokens = tokens
    def __str__(self):
        return f"{self.name}: {self.tokens} token(s)"

class Transicao:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
    
    def is_enabled(self):
        return all(place.tokens > 0 for place in self.inputs)
    
    def fire(self):
        if self.is_enabled():
            for place in self.inputs:
                place.tokens -= 1
            for place in self.outputs:
                place.tokens += 1
            print(f"Transição {self.name} disparada com sucesso.")
        else:
            print(f"Transição {self.name} não pode ser disparada. Tokens insufiencientes.")

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = []
    
    def add_place(self, place):
        self.places[place.name] = place

    def add_transition(self, transition):
        self.transitions.append(transition)
    
    def show_state(self):
        print("\nEstado atual da rede: ")
        for place in self.places.values():
            print(f" - {place}")
        print()

    def aidcionar_pedidos(self, quantidade):
        if "Entrada" in self.places:
            self.places['Entrada'].tokens += quantidade
            print(f"{quantidade} novo(s) pedido(s) aidcionado(s) à entrada.")
        else:
            print("Lugar 'Entrada' não existe na rede.")
    
    def run_interactive(self):
        print("\nModo Interativo Iniciado")
        print("Comandos disponíveis:")
        print("Digite o nome da transição para dispará-la:")
        print("Digite 'Novo X' para adicionar X pedidos na entrada.")
        print("Digite 'Status' para ver o estado atual da rede.")
        print("Digite 'Sair' para encerrar o programa. \n")

        operando = True
        while operando:
            comando = input("Comando: ").strip()
            if comando.capitalize() == 'Sair':
                print("Encerrando...")
                operando = False
                break
            elif comando.capitalize() == 'Status':
                self.show_state()
            elif comando.capitalize().startswith("Novo"):
                try:
                    qtd = int(comando.split()[1])
                    self.aidcionar_pedidos(qtd)
                except(IndexError, ValueError):
                    print("Use o comando no formato: novo <quantidade>.")
            else:
                transicao_encontrada = False
                for t in self.transitions:
                    if t.name.capitalize() == comando.capitalize():
                        t.fire()
                        transicao_encontrada = True
                        break
                    if not transicao_encontrada:
                        print("Transição não encontrada. Tente novamente.")

entrada = Place("Entrada", tokens=1)
espera = Place("Espera")
processamento = Place("Processamento")
envio = Place("Envio")

rede = PetriNet()
for p in [entrada, espera, processamento, envio]:
    rede.add_place(p)

t_receber = Transicao("Receber Pedido", [entrada], [espera])
t_processar = Transicao("Processar Pedido", [espera], [processamento])
t_enviar = Transicao("Enviar Pedido", [processamento], [envio])

for t in [t_receber, t_processar, t_enviar]:
    rede.add_transition(t)

rede.run_interactive()