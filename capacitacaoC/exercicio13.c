#include <stdio.h>

int main(void) {
    char nome[] = "Luiz Gustavo Morais Vasconcelos";
    int quantiaLetraA = 0;
    for (int i = 0; i <= (sizeof(nome) / sizeof(nome[0])); i++) {
        if (nome[i] == 'a') {
            quantiaLetraA++;
        }
    }
    printf("No nome %s, a letra a (minúscula) aparece %d vezes\n", nome, quantiaLetraA);
    return 0;
}