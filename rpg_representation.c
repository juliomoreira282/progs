#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_NOME 20

struct jogador {
    char nome[MAX_NOME];
    int id;
    int level;
    int hp;
    int atk;
    int def;
};

void imprimir(struct jogador j) {
    printf("Nome: %s", j.nome);
    printf("ID: %d\n", j.id);
    printf("Level: %d\n", j.level);
    printf("Vida: %d\n", j.hp);
    printf("Ataque: %d\n", j.atk);
    printf("Defesa: %d\n", j.def);
}
int main() {
    int personagens;
    struct jogador j1;
    printf("Insira a quantidade de personagens a ser adicionada: \n");
    scanf("%d", &personagens);
    for(int i = 0; i < personagens; i++) {
        getchar();
        printf("Nome: ");
        fgets(j1.nome, MAX_NOME, stdin);
        printf("ID: ");
        scanf("%d", &j1.id);
        printf("Level: ");
        scanf("%d", &j1.level);
        printf("Vida: ");
        scanf("%d", &j1.hp);
        printf("Ataque: ");
        scanf("%d", &j1.atk);
        printf("Defesa: ");
        scanf("%d", &j1.def);

        imprimir(j1);
    }

    return 0;
}