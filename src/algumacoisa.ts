class Animal {
    constructor(public nome: string) { }
    mover(distanciaEmMetros: number = 0) {
        console.log(`${this.nome} moveu ${distanciaEmMetros}m.`);
    }
}
class Cobra extends Animal {
    constructor(public nome: string) { super(nome); }
    mover(distanciaEmMetros = 5) {
        console.log("Rastejando...");
        super.mover(distanciaEmMetros);
    }
}