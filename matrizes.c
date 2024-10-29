#include <stdio.h>
int main() {
    int matriz[3][3];
    printf("Digite os elementos da matriz: \n");
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            scanf("%d", &matriz[i][j]);
        }
    }

    int somaLinha2 = 0;
    for(int j = 0; j < 3; j++) {
        somaLinha2 += matriz[1][j];
    }
    printf("Soma da Linha 2: %d \n", somaLinha2);

    int somaColuna1 = 0;
    for(int i = 0; i < 3; i++) {
        somaColuna1 += matriz[i][0];
    }
    printf("Soma da Coluna 1: %d \n", somaColuna1);

    int somaDiagonalPrincipal = 0;
    for(int i = 0; i < 3; i++) {
        somaDiagonalPrincipal += matriz[i][i];
    }
    printf("Soma da Diagonal Principal: %d \n", somaDiagonalPrincipal);

    int somaDiagonalSecundaria = 0;
    for(int i = 0; i < 3; i++) {
        somaDiagonalSecundaria += matriz[i][2 - i];
    }
    printf("Soma da Diagonal Secundária: %d \n", somaDiagonalSecundaria);

    int somaTotal = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            somaTotal += matriz[i][j];
        }
    }
    printf("Soma de Todos os Elemetos da Matriz: %d \n", somaTotal);

    return 0;
}