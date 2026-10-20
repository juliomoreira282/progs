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
            print(f"Transição {self.name} não pode ser disparada. Tokens insuficientes.")

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = []

    def add_place(self, place):
        self.places[place.name] = place

    def add_transition(self, transition):
        self.transitions.append(transition)

    def show_state(self):
        print("\nEstado atual da rede:")
        for place in self.places.values():
            print(f" - {place}")
        print()

    def adicionar_pedidos(self, quantidade: int):
        if "entrada" in self.places:
            self.places["entrada"].tokens = quantidade
            print(f"{quantidade} novos pedido(s) adicionado(s) à rede.")
        else:
            print("Valor 'entrada' não existe na rede.")

    def transition_handling(self, comando: str):
        transicao_encontrada = False
        for t in self.transitions:
            if comando.lower() == t.name.lower():
                t.fire()
                transicao_encontrada = True
                break
            if not transicao_encontrada:
                print("Transição não encontrada. Tente novamente.")

def main():
    entrada = Place("entrada", tokens=1)
    espera = Place("espera")
    processamento = Place("processamento")
    envio = Place("envio")

    rede = PetriNet()
    for p in [entrada, espera, processamento, envio]:
        rede.add_place(p)

    t_receber = Transicao("receber", [entrada], [espera])
    t_processar = Transicao("processar", [espera], [processamento])
    t_enviar = Transicao("enviar", [processamento], [envio])

    for t in [t_receber, t_processar, t_enviar]:
        rede.add_transition(t)
    
    print("\nModo interativo iniciado")
    print("Comandos disponíveis:")
    print("Digite o nome da transição para dispará-la.")
    print("Digite 'novo X' para adicionar novos pedidos.")
    print("Digite 'status' para ver o estado atual da rede.")
    print("Digite 'sair' para encerrar o programa.")

    operando = True
    while operando:
        comando = input("Comando: ").strip()
        if comando.lower() == "sair":
            print("Encerrando...")
            operando = False
        elif comando.lower() == "status":
            rede.show_state()
        elif comando.lower().startswith("novo"):
            try:
                qtd = int(comando.split()[1])
                rede.adicionar_pedidos(qtd)
            except (IndexError, ValueError):
                print("Use o comando no formato: novo <quantidade>.")
        else:
            rede.transition_handling(comando)

if __name__ == "__main__":
    main()