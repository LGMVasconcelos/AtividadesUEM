#include <stdio.h>
#include <stdbool.h>
#include "aula.c"

int main() {
    float horaInicioAula1, horaFimAula1, horaInicioAula2, horaFimAula2;
    
    do {
        printf("Digite o horário de início da primeira aula (em horas): ");
        scanf("%f", &horaInicioAula1);
        printf("Digite o horário de fim da primeira aula (em horas): ");
        scanf("%f", &horaFimAula1);
        if (!validaHorario(horaInicioAula1, horaFimAula1)) {
            printf("Horário de aula inválido! Tente novamente\n\n");
        }
    } while (!validaHorario(horaInicioAula1, horaFimAula1));

    printf("\n");

    do {
        printf("Digite o horário de início da segunda aula (em horas): ");
        scanf("%f", &horaInicioAula2);
        printf("Digite o horário de fim da segunda aula (em horas): ");
        scanf("%f", &horaFimAula2);
        if (!validaHorario(horaInicioAula2, horaFimAula2)) {
            printf("Horário de aula inválido! Tente novamente\n\n");
        }
    } while (!validaHorario(horaInicioAula2, horaFimAula2));

    if (aulasConflitam(horaInicioAula1, horaFimAula1, horaInicioAula2, horaFimAula2)) {
        printf("O agendamento das duas aulas não pode ocorrer, pois os horários de aula estão conflitando entre si.\n");
    }
    else {
        printf("Aula agendada com sucesso.\n");
    }

    return 0;
}