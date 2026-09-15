from fila import Fila
from pilha import Pilha


def inverter_fila(fila: Fila) -> Fila:
    """
    Inverte a ordem dos elementos de uma fila.

    A transformação deve utilizar exclusivamente as operações
    disponibilizadas pelos TADs Fila e Pilha.

    A fila recebida deve ser modificada e retornada pela função.

    Parâmetros:
        fila: fila que terá seus elementos invertidos.

    Retorna:
        A própria fila, com os elementos em ordem inversa.

    Exemplos:
        >>> fila = Fila()
        >>> fila.enqueue("A")
        >>> fila.enqueue("B")
        >>> fila.enqueue("C")
        >>> inverter_fila(fila)
        Fila(['C', 'B', 'A'])

        >>> fila = Fila()
        >>> fila.enqueue(1)
        >>> fila.enqueue(2)
        >>> fila.enqueue(3)
        >>> inverter_fila(fila)
        Fila([3, 2, 1])

    Observação:
        Não é permitido acessar diretamente a representação
        interna da Fila ou da Pilha.
    """
    pilha_auxiliar = Pilha(len(fila))

    while not fila.is_empty():
        pilha_auxiliar.push(fila.dequeue())

    while not pilha_auxiliar.is_empty():
        fila.enqueue(pilha_auxiliar.pop())

    return fila