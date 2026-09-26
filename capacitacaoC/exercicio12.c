#include <stdio.h>

int main(void) {
    int numeros[5] = {1, 2, 3, 4, 5};
    int soma = 0;
    for (int i = 0; i <= 5; i++) {
        soma += numeros[i];
    }
    printf("A soma é %d\n", soma);
    return 0;
}