#include <stdio.h>

void somar() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 + n2;
    printf("O resultado da soma é %.2f\n", resultado);
}

void subtrair() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 - n2;
    printf("O resultado da subtração é %.2f\n", resultado);
}

void multiplicar() {
    float n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%f", &n1);
    printf("Digite o segundo número: ");
    scanf("%f", &n2);
    float resultado = n1 * n2;
    printf("O resultado da multiplicação é %.2f\n", resultado);
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
        printf("O resultado da divisão é %.2f\n", resultado);
    }
    
}

int main() {
    int n;

    do {
        printf("==========CALCULADORA==========\n\nDigite 0 para sair e de 1 a 4 para realizar as respectivas operações com 2 números:\n0 - Sair\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite aqui: ");
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
        case 0:
            printf("Saindo da calculadora...\n");
            break;
        default:
            printf("Opção inválida.\n");
            break;
        }
    } while (n != 0);

    return 0;
}