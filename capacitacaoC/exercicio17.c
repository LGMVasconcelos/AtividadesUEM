#include <stdio.h>

float calcularMedia(float *arr, int tamanho) {
    float soma = 0.0;
    for (int i = 0; i <= tamanho; i++) {
        if (arr[i] > 0) {
            soma += arr[i];
        }
    }
    return soma / tamanho;
}

int main(void) {
    float notas[] = {7.0f, 9.5f, 4.5f, 6.7f, 8.0f};
    for (int i = 0; i < (sizeof(notas) / sizeof(notas[0])); i++) {
        printf("Nota %d: %.1f\n", i + 1, notas[i]);
    }
    printf("Média das notas: %.1f\n", calcularMedia(notas, (sizeof(notas) / sizeof(notas[0]))));
}