#include <stdio.h>
int main() {
    int linhas, colunas;
    int matriz[linhas][colunas];

    printf("Digite a quantidade de linhas da matriz: \n");
    scanf("%d", &linhas);

    printf("Digite a quantidade de linhas da matriz: \n");
    scanf("%d", &colunas);

    if(linhas != colunas) {
        printf("Essa matriz não é quadrada. \n");
    }
    else {
        printf("Digite os elementos da matriz: \n");
        for(int i = 0; i < linhas; i++) {
            for(int j = 0; j < colunas; j++) {
                scanf("%d", &matriz[i][j]);
            }
        }
        int somaDiagonalPrincipal = 0;
        for(int i = 0; i < linhas; i++) {
            somaDiagonalPrincipal += matriz[i][i];
        }
        printf("Soma da Diagonal Principal: %d \n", somaDiagonalPrincipal);
    }
    return 0;
}