#include <stdio.h>

void positivoParaNegativo(int *arr, int tamanho) {
    for (int i = 0; i <= tamanho; i++) {
        if (arr[i] > 0) {
            arr[i] = -arr[i];
        }
    }
}

int main(void) {
    int numeros[] = {1, -2, 4, 5, 0};
    for (int i = 0; i < (sizeof(numeros) / sizeof(numeros[0])); i++) {
        printf("Valor %d: %d\n", i + 1, numeros[i]);
    }
    printf("Convertendo os valores positivos para negativos...\n");
    positivoParaNegativo(numeros, (sizeof(numeros) / sizeof(numeros[0])));
    for (int i = 0; i < (sizeof(numeros) / sizeof(numeros[0])); i++) {
        printf("Valor %d: %d\n", i + 1, numeros[i]);
    }
} 