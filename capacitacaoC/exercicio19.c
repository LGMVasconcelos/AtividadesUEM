#include <stdio.h>
#include <string.h>
typedef struct Produto {
    char nome[50];
    float preco;
    int quantidade;
} Produto;

int main() {
    Produto produtos[5];
    float precoTotal;
    for (int i = 0; i < 5; i++) {
        printf("Digite o nome do produto %d: ", i + 1);
        fgets(produtos[i].nome, 50, stdin);
        produtos[i].nome[strcspn(produtos[i].nome, "\n")]  = '\0';

        printf("Digite o preço do produto %d: ", i + 1);
        scanf("%f", &produtos[i].preco);

        printf("Digite a quantidade do produto %d no estoque: ", i + 1);
        scanf("%d", &produtos[i].quantidade);

        getchar(); 
        printf("\n");
    }
    for (int i = 0; i < 5; i++) {
        precoTotal = produtos[i].preco * produtos[i].quantidade;
        printf("Preço total do produto %d (%s): %2.f\n", i + 1, produtos[i].nome, precoTotal);
    }
    return 0;
}