#include <math.h>
#include <stdio.h>

typedef struct Ponto {
    float x;
    float y;
} Ponto;

int main() {
    Ponto p1, p2;
    float distancia;

    printf("Digite as coordenadas do primeiro ponto (x,y): ");
    scanf("%f %f", &p1.x, &p1.y);

    printf("Digite as coordenadas do segundo ponto (x,y): ");
    scanf("%f %f", &p2.x, &p2.y);

    distancia = sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));

    printf("A distância entre os pontos é: %.2f\n", distancia);

    return 0;
}
