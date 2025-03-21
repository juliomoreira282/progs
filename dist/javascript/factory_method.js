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
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de latir e de brincar com meu dono ${this.nomeTutor}.`);
    }
}

class Gato extends Animal {
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto de dormir e de ignorar meu dono ${this.nomeTutor}.`);
    }
}

class Passaro extends Animal {
    comunicacao() {
        console.log(`Meu nome é ${this.nome} e meu dono é ${this.nomeTutor}.`);
    }
    comportamento() {
        console.log(`Gosto muito de cantar para meu dono ${this.nomeTutor}.`);
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
            default:
                return null;
        }
    }
}

const cachorro = AnimalFactory.criarAnimal("cachorro", "Leo", 9, "Francisco", "Grande");
cachorro.comunicacao();
cachorro.comportamento();

const gato = AnimalFactory.criarAnimal("gato", "Neve", 5, "William", "Pequeno");
gato.comunicacao();
gato.comportamento();

const passaro = AnimalFactory.criarAnimal("passaro", "Marcelo", 13, "Gabriel", "Médio");
passaro.comunicacao();
passaro.comportamento();