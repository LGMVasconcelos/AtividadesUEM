#include <stdio.h>

int main(void) {
    int incremento = 0;
    for (int i = 0; i <= 100; i++) {
        incremento += i;
    }
    printf("%d", incremento, "\n");
    return 0;
}