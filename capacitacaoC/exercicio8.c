#include <stdio.h>

void somar() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 + n2;
    printf("O resultado da soma é %f", resultado, "\n");
}

void subtrair() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 - n2;
    printf("O resultado da subtração é %f", resultado, "\n");
}

void multiplicar() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 * n2;
    printf("O resultado da multiplicação é %f", resultado, "\n");
}

void dividir() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    if (n2 == 0) {
        printf("Erro: Não é permitida a divisão por 0!\n");
    }
    else {
        float resultado = n1 / n2;
        printf("O resultado da divisão é %f", resultado, "\n");
    }
    
}

int main() {
    int n;
    printf("==========CALCULADORA==========\n\nDigite de 1 a 4 para realizar as respectivas operações com 2 números:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite aqui: ");
    scanf("%d", &n);
    switch (n) {
        case 1:
            somar();
            break;
        case 2:
            subtrair();
            break;
        case 3:
            multiplicar();
            break;
        case 4:
            dividir();
            break;
        default:
            printf("Opção inválida.\n");
    }
    return 0;
}