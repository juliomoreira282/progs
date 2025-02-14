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
    criarAnimal(_nome, _idade, _nomeTutor, _porte) {
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

function criarExibirAnimal(factory, nome, idade, nomeTutor, porte) {
    const animal = factory.criarAnimal(nome, idade, nomeTutor, porte);
    animal.comunicacao();
    animal.comportamento();
}

criarExibirAnimal(new FabricaCachorro(), "Hugo", 12, "Igor", "Pequeno");
criarExibirAnimal(new FabricaGato(), "Jujuba", 3, "Luisa", "Pequeno");