"use strict";
class Animal {
    constructor(nome) {
        this.nome = nome;
    }
    mover(distanciaEmMetros = 0) {
        console.log(`${this.nome} moveu ${distanciaEmMetros}m.`);
    }
}
class Cobra extends Animal {
    constructor(nome) {
        super(nome);
        this.nome = nome;
    }
    mover(distanciaEmMetros = 5) {
        console.log("Rastejando...");
        super.mover(distanciaEmMetros);
    }
}
