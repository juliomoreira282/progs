class Animal {
    constructor(nome, idade, nomeTutor, porte) {
        this.nome = nome;
        this.idade = idade;
        this.nomeTutor = nomeTutor;
        this.porte = porte;
    }

    comunicacao() {
        throw "Abstract Method";
    }
    comportamento() {
        throw "Abstract Method";
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
    criarAnimal(nome, idade, nomeTutor, porte) {
        throw "Abstract Method";
    }
}

class FabricaCachorro extends AnimalFactory {
    criarAnimal(nome, idade, nomeTutor, porte) {
        return new Cachorro(nome, idade, nomeTutor, porte);
    }
}

class FabricaGato extends AnimalFactory {
    criarAnimal(nome, idade, nomeTutor, porte) {
        return new Gato(nome, idade, nomeTutor, porte);
    }
}

class FabricaPassaro extends AnimalFactory {
    criarAnimal(nome, idade, nomeTutor, porte) {
        return new Passaro(nome, idade, nomeTutor, porte);
    }
}

function criarExibirAnimal (factory, nome, idade, nomeTutor, porte) {
    const animal = factory.criarAnimal(nome, idade, nomeTutor, porte);
    animal.comunicacao();
    animal.comportamento();
}

criarExibirAnimal(new FabricaCachorro(), "Bebeto", 8, "Marcelo", "Médio");
criarExibirAnimal(new FabricaGato(), "Bolinha", 7, "Tifa", "Pequeno");
criarExibirAnimal(new FabricaPassaro(), "Juninho", 10, "Denise", "Médio");