#include <stdbool.h>
#include "funcoesaula.h"

bool validaHorario(float horaInicio, float horaFim) {
    return horaInicio >= 7 && horaFim <= 18 && horaInicio < horaFim;
}

bool aulasConflitam(float horaInicio1, float horaFim1, float horaInicio2, float horaFim2) {
    return horaInicio1 < horaFim2 && horaInicio2 < horaFim1;
}