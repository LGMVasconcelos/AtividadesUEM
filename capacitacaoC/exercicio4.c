#include <stdio.h>

int main() {
    char nome[50];
    puts("Digite seu nome:");
    fgets(nome, 50, stdin);
    printf("Seu nome é %s", nome, "!");
    return 0;
}