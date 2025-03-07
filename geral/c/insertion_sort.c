#include <stdio.h>

void printArray(int array[], int n) {
    for(int i = 0; i < n; i++) {
        printf("%d", array[i]);
        if(i < n - 1) {
            printf(" | ");
        }
    }
    printf("\n");
}

void insertionSort(int array[], int n) {
    int aux;
    for(int i = 1; i < n; i++) {
        aux = array[i];
        int j = i - 1;

        printf("\nChave: %d\n", aux);
        printf("Estado Atual: ");
        printArray(array, n);

        while(j >= 0 && array[j] > aux) {
            array[j + 1] = array[j];
            j = j - 1;
            array[j + 1] = aux;
            printArray(array, n);
        }
    }
}

int main() {
    int array[8];

    for(int i = 0; i < 8; i++) {
        scanf("%d", &array[i]);
    }

    insertionSort(array, 8);

    printf("\nResultado Final: \n");
    printArray(array, 8);

    return 0;
}