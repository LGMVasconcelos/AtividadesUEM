#include <stdlib.h>
#include <stdio.h>

void solicitarTamanho(int *arr, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("Digite o elemento de nº %d da lista: ", i + 1);
        scanf("%d", &arr[i]);
        getchar();
    }
}

int main() {
    int tamanho;
    printf("Digite o tamanho desejado para a lista: ");
    scanf("%d", &tamanho);
    printf("\n");
    int *lst = malloc( tamanho * sizeof(int));
    solicitarTamanho(lst, tamanho);
    printf("lista final: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", lst[i]);
    }
    printf("\n");
    free (lst);
    lst = NULL;
    return 0;
}
