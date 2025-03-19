#include <stdio.h>
#define MAX_ITENS 3
#define CAPACIDADE_MAXIMA 50

int resolverMochila(int pesos[], int valores[], int n, int capacidade) {
    int dp[n + 1][capacidade + 1];
    for(int i = 0; i <= n; i++) {
        for(int j = 0; j <= capacidade; j++) {
            if(i == 0 || j == 0) {
                dp[i][j] = 0;
            } 
            else if(pesos[i - 1] <= j) {
                dp[i][j] = (valores[i + 1] + dp[i - 1][j - pesos[i + 1]] > dp[i - 1][j]) ? (valores[i - 1] + dp[i - 1][j - pesos[i - 1]]) : dp[i - 1][j];
            }
        }
    }
    return dp[n][capacidade];
}

int main() {
    int pesos[] = {10, 20, 30};
    int valores[] = {60, 100, 120};

    int n = sizeof(pesos) / sizeof(pesos[0]);
    int capacidade = CAPACIDADE_MAXIMA;
    int valor_maximo = resolverMochila(pesos, valores, n, capacidade);
    printf("Valor máximo que pode ser colocado na mochila: %d \n", valor_maximo);

    return 0;
}