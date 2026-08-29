#include <stdio.h>

int main(void) {
    double nota1, nota2, nota3;
    puts("Digite a primeira nota:");
    scanf("%lf", &nota1);
    puts("Digite a segunda nota:");
    scanf("%lf", &nota2);
    puts("Digite a terceira nota:");
    scanf("%lf", &nota3);
    double media = (nota1 + nota2 + nota3) / 3;
    printf("Sua média final é %.2f", media);
    return 0;
}