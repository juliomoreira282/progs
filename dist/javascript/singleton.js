class Animal {
    constructor(nome, idade, nomeTutor, porte) {
        this.nome = nome;
        this.idade = idade;
        this.nomeTutor = nomeTutor;
        this.porte = porte;
    }
    comunicacao() {
        console.log("Sou um animal, portanto, faço barulho.");
    }
    comportamento() {
        console.log("Essa é minha forma de agir.");
    }
}

class Cachorro extends Animal {
    static instance = null;
    constructor(nome, idade, nomeTutor, porte) {
        if(!Cachorro.instance) {
            super(nome, idade, nomeTutor, porte);
            Cachorro.instance = this;
        }
        return Cachorro.instance;
    }
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de latir e de brincar com meu dono ${this.nomeTutor}.`);
    }
}

class Gato extends Animal {
    static instance = null;
    constructor(nome, idade, nomeTutor, porte) {
        if(!Gato.instance) {
            super(nome, idade, nomeTutor, porte);
            Gato.instance = this;
        }
        return Gato.instance;
    }
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de dormir e de deixar meu dono ${this.nomeTutor} no vácuo.`);
    }
}

class Passaro extends Animal { 
    static instance = null;
    constructor(nome, idade, nomeTutor, porte) {
        if(!Passaro.instance) {
            super(nome, idade, nomeTutor, porte);
            Passaro.instance = this;
        }
        return Passaro.instance;
    }
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto muito de cantar para meu dono ${this.nomeTutor}.`);
    }
}

const c1 = new Cachorro("Leo", 8, "Francisco", "Grande");
const c2 = new Cachorro("Bibi", 5, "Roberto", "Pequeno");
console.log(c1 === c2);
c1.comunicacao();
c2.comunicacao();
c1.comportamento();
c2.comportamento();

const g1 = new Gato("Neve", 5, "William", "Pequeno");
const g2 = new Gato("Fuligem", 10, "Gustavo", "Médio");
console.log(g1 === g2);
g1.comunicacao();
g2.comunicacao();
g1.comportamento();
g2.comportamento();

const p1 = new Passaro("Marcelo", 13, "Gabriel", "Pequeno");
const p2 = new Passaro("Dida", 23, "Daniel", "Grande");
console.log(p1 === p2);
p1.comunicacao();
p2.comunicacao();
p1.comportamento();
p2.comportamento();