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
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu/minha dono(a) é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de latir e de brincar com meu/minha dono(a) ${this.nomeTutor}.`);
    }
}

class Gato extends Animal {
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu/minha dono(a) é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de dormir e de ignorar meu/minha dono(a) ${this.nomeTutor}.`);
    }
}

class Passaro extends Animal {
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu/minha dono(a) é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto muito de cantar para meu/minha dono(a) ${this.nomeTutor}.`);
    }
}

class AnimalFactory {
    static criarAnimal(tipo, nome, idade, nomeTutor, porte) {
        switch(tipo.toLowerCase()) {
            case "cachorro":
                return new Cachorro(nome, idade, nomeTutor, porte);
            case "gato":
                return new Gato(nome, idade, nomeTutor, porte);
            case "passaro":
                return new Passaro(nome, idade, nomeTutor, porte);
        }
    }
}

const c = AnimalFactory.criarAnimal("cachorro", "Bebeto", 8, "Marcelo", "Médio");
c.comunicacao();
c.comportamento();

const g = AnimalFactory.criarAnimal("gato", "Bolinha", 7, "Tifa", "Pequeno");
g.comunicacao();
g.comportamento();

const p = AnimalFactory.criarAnimal("passaro", "Juninho", 10, "Denise", "Pequeno");
p.comunicacao();
p.comportamento();