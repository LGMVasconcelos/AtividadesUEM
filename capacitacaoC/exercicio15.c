#include <stdio.h>

void trocarValores(int *int1, int *int2) {
    int aux = *int1;
    *int1 = *int2;
    *int2 = aux;
}

int main(void) {
    int valor1 = 5;
    int valor2 = 10;
    printf("Valor 1: %d, valor 2: %d\n", valor1, valor2);
    trocarValores(&valor1, &valor2);
    printf("Valor 1: %d, valor 2: %d\n", valor1, valor2);
    return 0;
}