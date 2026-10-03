#include <stdio.h>
#include <stdlib.h>

int main() {
    int capacidade = 3;
    int quantiaElementos = 0;
    int *arr = malloc(capacidade * sizeof(int));
    int resultado;

    if (arr == NULL) {
        printf("Erro ao alocar memoria!\n");
        return 1;
    }

    printf("Digite os elementos (digite -1 para parar):\n");
    while (1) {
        printf("Elemento de no %d: ", quantiaElementos + 1);
        
        if (scanf("%d", &resultado) != 1) {
            printf("Entrada invalida!\n");
            break;
        }

        if (resultado == -1) {
            break;
        }

        if (quantiaElementos >= capacidade) {
            capacidade *= 2;
            int *temp = realloc(arr, capacidade * sizeof(int));
            if (temp == NULL) {
                printf("Erro ao realocar memoria!\n");
                free(arr);
                return 1;
            }
            arr = temp;
        }

        arr[quantiaElementos] = resultado;
        quantiaElementos++;
    }

    printf("Array final:\n");
    for (int i = 0; i < quantiaElementos; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);
    arr = NULL;
    return 0;
}
