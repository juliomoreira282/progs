class TuringMachine {
    constructor(tape, rules, startState, acceptState) {
        this.tape = tape;
        this.rules = rules;
        this.state = startState;
        this.acceptState = acceptState;
        this.head = 0;
    }
    step() {
        const currentSymbol = this.tape[this.head];
        const rule = this.rules[this.state]?.[currentSymbol];
        if(!rule) {
            console.log("Nenhuma regra encontrada. Máquina parou.");
            return false;
        }
        const[newSymbol, direction, newState] = rule;
        this.tape[this.head] = newSymbol;
        this.state = newState;
        if(direction == 'R') {
            this.head++;
        }
        else if(direction === 'L') {
            this.head--;
        }
    }
    run() {
        console.log(`Fita inicial: ${this.tape.join('')}`);
        while(this.state !== this.acceptState) {
            if(!this.step()) break;
            console.log(`Estado: ${this.state}, Fita: ${this.state.join('')}, Cabeçote em ${this.head}`);
        }
        if(this.state === this.acceptState) {
            console.log(`Máquina aceitou a fita: ${this.tape.join('')}`);
        }
        else {
            console.log(`Máquina parou sem aceitar.`)
        }
    }
}
const fita = ['A', 'B', 'C', '_', '_', '_'];
const regras = {
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
};
const estadoInicial = 'q0';
const estadoFinal = 'q2';
const maquina = new TuringMachine(fita, regras, estadoInicial, estadoFinal);
maquina.run();