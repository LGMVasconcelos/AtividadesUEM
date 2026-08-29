#include <stdio.h>

int main(void) {
    float preco;
    puts("Digite o preço do produto:");
    scanf("%f", &preco);
    float precoDescontado = preco * 0.9;
    printf("O preço do produto com desconto é de %2.f", precoDescontado);
    return 0;
}