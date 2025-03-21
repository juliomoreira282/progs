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

class AnimalFactory {
    static criarAnimal(nome, idade, nomeTutor, porte, tipo) {
        switch(tipo.toLowerCase()) {
            case "cachorro":
                return new Cachorro(nome, idade, nomeTutor, porte);
            case "gato":
                return new Gato(nome, idade, nomeTutor, porte);
            default:
                return null;
        }
    }
}

cachorro = AnimalFactory.criarAnimal("Plínio", 3, "Rodolfo", "Pequeno", "cachorro");
cachorro.comunicacao();
cachorro.comportamento();

gato = AnimalFactory.criarAnimal("Jujuba", 6, "Larissa", "Pequeno", "gato");
gato.comunicacao();
gato.comportamento();