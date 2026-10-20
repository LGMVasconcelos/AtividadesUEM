from __future__ import annotations

from typing import Generic, TypeVar

from lista_encadeada import ListaEncadeada

T = TypeVar("T")

class Conjunto(Generic[T]):
    """
    Tipo Abstrato de Dados Conjunto: coleção de elementos distintos,
    sem repetições e sem noção de posição.

    Representação: lista encadeada (ver lista_encadeada.py).

    Invariantes
    -----------
    - A lista nunca contém valores duplicados.
    - `__tamanho` é sempre igual ao número de nós da lista.

    Pré-requisito geral
    -------------------
    Os elementos devem ser comparáveis entre si (<, >), pois a lista
    depende dessa ordem.

    Operações que produzem novos conjuntos (uniao, intersecao, diferenca)
    NÃO modificam os conjuntos de entrada.

    Exemplos
    --------
    >>> A = Conjunto([1, 2, 3, 4])
    >>> B = Conjunto([3, 4, 5, 6])
    >>> A.uniao(B)
    Conjunto([1, 2, 3, 4, 5, 6])
    >>> A.intersecao(B)
    Conjunto([3, 4])
    >>> A.diferenca(B)
    Conjunto([1, 2])
    """
    
    def __init__(self, elementos_iniciais: list[T] | None = None) -> None:
        """
        Cria um conjunto, opcionalmente a partir de elementos iniciais.
        Elementos repetidos são ignorados.

        Exemplos
        --------
        >>> Conjunto()
        Conjunto([])

        >>> Conjunto([3, 1, 3, 2, 1])
        Conjunto([1, 2, 3])
        """
        self.__lista: ListaEncadeada[T] = ListaEncadeada()
        self.__tamanho = 0
        if elementos_iniciais is not None:
            for elemento in elementos_iniciais:
                self.inserir(elemento)
                
    