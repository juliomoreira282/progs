#include <stdio.h>
int main() {
    int idade;
    
    printf("Digite a idade do usuário: \n");
    scanf("%d", &idade);

    if(idade >= 16 && idade < 18) {
        printf("O voto é facultativo. \n");
    }
    else if(idade >= 18) {
        printf("O voto é obrigatório. \n");
    }
    else {
        printf("Não pode votar. \n");
    }

    return 0;
}