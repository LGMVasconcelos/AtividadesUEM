#include <stdio.h>

int main() {
    int n;
    printf("Insira um número inteiro: ");
    scanf("%d", &n);
    if (n > 0) {
        printf("O número é positivo.");
    }
    else if (n < 0) {
        printf("O número é negativo.");
    }
    else {
        printf("O valor inserido é 0.");
    }
    return 0;
}