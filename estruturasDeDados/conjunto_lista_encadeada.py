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
                
    def elementos(self, inicio: int, fim: int) -> list[T]:
        """
        Retorna uma lista com os elementos do conjunto.

        Exemplos
        --------
        >>> A = Conjunto([3, 1, 2])
        >>> A.elementos()
        [1, 2, 3]
        """
        pivo = self.__lista.inicio
        i = 0
        elementos: ListaEncadeada[T] = ListaEncadeada()
        while pivo is not None and i < fim:
            if i >= inicio:
                elementos.inserir(pivo.dado)
            pivo = pivo.proximo
            i += 1

        def quicksort(esquerda: int, direita: int) -> None:
            if esquerda >= direita:
                return

            indice_pivo = (esquerda + direita) // 2
            valor_pivo = elementos[indice_pivo]
            menor, maior = esquerda, direita

            while menor <= maior:
                while elementos[menor] < valor_pivo:
                    menor += 1
                while elementos[maior] > valor_pivo:
                    maior -= 1
                if menor <= maior:
                    elementos[menor], elementos[maior] = (
                        elementos[maior], elementos[menor]
                    )
                    menor += 1
                    maior -= 1

            if esquerda < maior:
                quicksort(esquerda, maior)
            if menor < direita:
                quicksort(menor, direita)

        if elementos:
            quicksort(0, len(elementos) - 1)
        return elementos