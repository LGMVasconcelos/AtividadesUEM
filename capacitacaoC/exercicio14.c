#include <stdio.h>

int main(void) {
    int pontuacao = 100;
    int *ponteiro = &pontuacao;
    printf("%d\n", *ponteiro);

    *ponteiro = 50;

    printf("%d\n", pontuacao);

    return 0;
}