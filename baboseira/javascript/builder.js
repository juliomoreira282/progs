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
        console.log("Essa é minha forma de agir");
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
        console.log(`Gosto de dormir e de deixar meu dono ${this.nomeTutor} no vácuo.`);
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

class AnimalBuilder {
    constructor() {
        this.nome = null;
        this.idade = null;
        this.nomeTutor = null;
        this.porte = null;
        this.tipoAnimal = null;
    }
    
    setNome(nome) {
        this.nome = nome;
        return this;
    }
    
    setIdade(idade) {
        this.idade = idade;
        return this;
    }

    setNomeTutor(nomeTutor) {
        this.nomeTutor = nomeTutor;
        return this;
    }

    setPorte(porte) {
        this.porte = porte;
        return this;
    } 

    setTipoAnimal(tipoAnimal) {
        this.tipoAnimal = tipoAnimal;
        return this;
    }

    build() {
        switch(this.tipoAnimal.toLowerCase()) {
            case "cachorro":
                return new Cachorro(this.nome, this.idade, this.nomeTutor, this.porte);
            case "gato":
                return new Gato(this.nome, this.idade, this.nomeTutor, this.porte);
            case "passaro":
                return new Passaro(this.nome, this.idade, this.nomeTutor, this.porte);
            default:
                throw new Error("Tipo de animal inválido. Use apenas 'Cachorro', 'Gato' ou 'Passaro'.");
        }
    }
}

const builder = new AnimalBuilder();

const cachorro = builder
    .setNome("Leo")
    .setIdade(8)
    .setNomeTutor("Francisco")
    .setPorte("Grande")
    .setTipoAnimal("cachorro")
    .build();
cachorro.comunicacao();
cachorro.comportamento();

const gato = builder
    .setNome("Neve")
    .setIdade(5)
    .setNomeTutor("William")
    .setPorte("Pequeno")
    .setTipoAnimal("gato")
    .build();
gato.comunicacao();
gato.comportamento();

const passaro = builder
    .setNome("Marcelo")
    .setIdade(13)
    .setNomeTutor("Gabriel")
    .setPorte("Pequeno")
    .setTipoAnimal("passaro")
    .build();
passaro.comunicacao();
passaro.comportamento();