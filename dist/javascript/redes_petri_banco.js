class CaixaEletronicoPetri {
    constructor(saldoInicial = 0.0) {
        this.saldo = saldoInicial;
        this.places = {
            saldo: saldoInicial,
            deposito: 0,
            saque: 0,
            consulta: 0
        };
    }

    depositar(valor) {
        this.places.deposito += valor;
        this.places.saldo += valor;
        console.log(`Depósito de R$ ${valor} realizado. Saldo atual: R$ ${this.places.saldo} \n`);
    }

    sacar(valor) {
        if(this.places.saldo >= valor) {
            this.places.saque += valor;
            this.places.saldo -= valor;
            console.log(`Saque de R$ ${valor} realizado. Saldo atual: R$ ${this.places.saldo} \n`);
        }
        else {
            console.log("Saldo insuficiente");
        }
    }

    consultar_saldo() {
        this.places.consulta += 1;
        console.log(`Saldo atual: R$ ${this.places['Saldo']} \n`);
    }

    definir_saldo_inicial() {
        const prompt = require('prompt-sync')();
        const valor = parseFloat(prompt("Informe o saldo inicial: "));
        this.saldo = valor;
        this.places.saldo = valor;
        console.log(`Saldo inicial definido como R$ ${this.places.saldo}. \n`);
    }

    menu() {
        const prompt = require('prompt-sync')();
        operando = true;
        while(operando) {
            console.log("Caixa Eletrônico");
            console.log("1. Depositar");
            console.log("2. Sacar");
            console.log("3. Consultar Saldo");
            console.log("4. Sair");
            const opcao = prompt("Escolha uma opção: ");
            switch(opcao) {
                case "1":
                    const valor = parseFloat(prompt("Informe o valor do depósito: "));
                    this.depositar(valor);
                case "2":
                    valor = parseFloat(prompt("Informe o valor do saque: "));
                    this.sacar(valor);
                case "3":
                    this.consultar_saldo();
                case "4":
                    console.log("Saindo...");
                    operando = false;
                    break;
                default:
                    console.log("Opção inválida. Tente novamente.");
            }
        }
    }
}

const caixa = new CaixaEletronicoPetri();
caixa.definir_saldo_inicial();
caixa.menu();