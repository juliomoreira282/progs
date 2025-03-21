class TuringMachine():
    def __init__(self, tape, rules, startState, acceptState):
        self.tape = tape
        self.rules = rules
        self.state = startState
        self.acceptState = acceptState
        self.head = 0
    
    def step(self):
        currentSymbol = self.tape[self.head]
        rule = self.rules.get(self.state, {}).get(currentSymbol)
        if not rule:
            print("Nenhuma regra encontrada. Máquina parou.")
            return False
        newSymbol, direction, newState = rule
        self.tape[self.head] = newSymbol
        self.state = newState
        if direction == 'R':
            self.head += 1
        elif direction == 'L':
            self.head -= 1
        return True
    
    def run(self):
        print(f"Fita Inicial: {''.join(self.tape)}")
        while self.state != self.acceptState:
            if not self.step():
                break
            print(f"Estado: {self.state}, Fita: {''.join(self.tape)}, Cabeçote em: {self.head}")
        if self.state == self.acceptState:
            print(f"Máquina aceitou a fita: {''.join(self.tape)}")
        else:
            print("Máquina parou sem aceitar.")

fita = ['A', 'B', 'C', '_', '_', '_']
regras = {
    'q0': {
        'A': ['B', 'R', 'q1'],
        'B': ['A', 'R', 'q1'],
        'C': ['C', 'R', 'q2'],
        '_': ['_', 'R', 'qf']
    },
    'q1': {
        'A': ['A', 'R', 'q1'],
        'B': ['C', 'L', 'q0'],
        'C': ['B', 'R', 'qf']
    },
    'q2': {
        'A': ['C', 'L', 'q1'],
        'B': ['A', 'R', 'qf'],
        '_': ['_', 'R', 'qf']
    },
}

estadoInicial = 'q0'
estadoFinal = 'q2'
maquina = TuringMachine(fita, regras, estadoInicial, estadoFinal)
maquina.run()