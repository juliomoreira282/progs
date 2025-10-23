const readline = require('readline');

class Place {
    constructor(name, tokens=0) {
        this.name = name;
        this.tokens = tokens;
    }

    toString() {
        return `${this.name}: ${this.tokens} token(s)`;
    }
}

class Transicao {
    constructor(name, inputs, outputs) {
        this.name = name;
        this.inputs = inputs;
        this.outputs = outputs;
    }

    isEnabled() {
        return this.inputs.every(place => place.tokens > 0);
    }

    fire() {
        if(this.isEnabled()) {
            this.inputs.forEach(place => {
                place.tokens -= 1;
            });
            this.outputs.forEach(place =>{
                place.tokens += 1;
            });
            console.log(`Transição ${this.name} disparada com sucesso.`);
        }
        else {
            console.log(`Transição ${this.name} não pode ser disparada. Tokens insuficientes.`);
        }
    }
}

class PetriNet {
    constructor() {
        this.places = {};
        this.transitions = [];
    }

    addPlace(place) {
        this.places[place.name] = place;
    }

    addTransition(transition) {
        this.transitions.push(transition);
    }

    showState() {
        console.log("\nEstado atual da rede: ");
        Object.values(this.places).forEach(place => {
            console.log(` - ${place}`);
        });
        console.log();
    }

    adicionarPedidos(quantidade) {
        if("entrada" in this.places) {
            this.places['entrada'].tokens += quantidade;
            console.log(`${quantidade} novo(s) pedidos adicionados à rede.`);
        }
        else {
            console.log("Lugar 'entrada' não existe na rede.");
        }
    }

    menuInterativo() {
        console.log("\nMenu interativo iniciado:");
        console.log("Comandos disponíveis:")
        console.log("Digite o nome da transição para dispará-la: 'receber pedido', 'processar pedido', 'enviar pedido'");
        console.log("Digite 'novo X' para adicionar novos pedidos à rede.");
        console.log("Digite 'status' para mostrar o estado atual da rede.");
        console.log("Digite 'sair' para encerrar.");

        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        const promptUser = () => {
            rl.question("Comando: ", (comando) => {
                const comandoLimpo = comando.trim();
                const comandoLower = comando.toLowerCase();

                if(comandoLower === 'sair') {
                    console.log("Encerrando...");
                    rl.close();
                    return;
                }

                if(comandoLower === 'status') {
                    this.showState();
                }

                else if(comandoLower.startsWith('novo')) {
                    const partes = comandoLimpo.split('');
                    if(partes.length === 2 && !isNaN(partes[1])) {
                        const qtd = parseInt(partes[1], 10);
                        this.adicionarPedidos(qtd);
                    }

                    else {
                        console.log("Use o comandono formato: novo <quantidade>.");
                    }
                }
                promptUser();
            });
        };
        promptUser();
    }
}

const entrada = new Place('entrada', 1);
const espera = new Place('espera');
const processamento = new Place('processamento');
const envio = new Place('envio');

const rede = new PetriNet();
[entrada, espera, processamento, envio].forEach(p => rede.addPlace(p));

const t_receber = new Transicao('receber pedido', [entrada], [espera]);
const t_processar = new Transicao('processar pedido', [espera], [processamento]);
const t_enviar = new Transicao('enviar pedido', [processamento], [envio]);

[t_receber, t_processar, t_enviar].forEach(t => rede.addTransition(t));

rede.menuInterativo();