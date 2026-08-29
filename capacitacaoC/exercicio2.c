int pronto = 0;
int guardado;


void marcarPronto(void) {
    pronto = 1;
}

void guardar(int valor) {
    guardado = valor;
}

int main(void) {
    marcarPronto();
    guardar(40);

    return 0;
}