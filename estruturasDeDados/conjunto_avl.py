from __future__ import annotations

from typing import Generic, Iterable, TypeVar

from avl import AVL


T = TypeVar("T")


class Conjunto(Generic[T]):
    """
    Tipo Abstrato de Dados Conjunto: coleção de elementos distintos,
    sem repetições e sem noção de posição.

    Representação: árvore AVL (ver avl.py).

    Invariantes
    -----------
    - A árvore nunca contém valores duplicados.
    - `__tamanho` é sempre igual ao número de nós da árvore.

    Pré-requisito geral
    -------------------
    Os elementos devem ser comparáveis entre si (<, >), pois a AVL
    depende dessa ordem.

    Operações que produzem novos conjuntos (uniao, intersecao, diferenca)
    NÃO modificam os conjuntos de entrada.

    Complexidade
    ------------
    Nas operações abaixo, n = tamanho de self, m = tamanho de `outro` e a
    altura da AVL é O(log n).

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

    def __init__(self, elementos_iniciais: Iterable[T] | None = None) -> None:
        """
        Cria um conjunto, opcionalmente a partir de elementos iniciais.
        Elementos repetidos são ignorados.

        Complexidade: O(k log k), com k = quantidade de elementos iniciais (k inserções de custo O(log k)).

        Exemplos
        --------
        >>> Conjunto()
        Conjunto([])

        >>> Conjunto([3, 1, 3, 2, 1])
        Conjunto([1, 2, 3])
        """
        self.__arvore: AVL[T] = AVL()
        self.__tamanho = 0
        if elementos_iniciais is not None:
            for elemento in elementos_iniciais:
                self.inserir(elemento)

    def elementos(self) -> list[T]:
        """
        Retorna os elementos em ordem crescente (nova lista).

        Complexidade: O(n log n) com o avl.py atual, pois o percurso em ordem
        concatena listas a cada nó (acumulando em uma única lista seria O(n)).

        Exemplos
        --------
        >>> Conjunto([30, 10, 20]).elementos()
        [10, 20, 30]

        >>> Conjunto().elementos()
        []
        """
        return self.__arvore.em_ordem()

    def inserir(self, x: T) -> None:
        """
        Insere `x` no conjunto, caso ainda não pertença a ele.
        Se `x` já estiver presente, o conjunto não é modificado.

        Complexidade: O(log n). A busca de duplicata e a inserção descem pela
        árvore, cuja altura é O(log n); o contador é O(1).

        Exemplos
        --------
        >>> A = Conjunto[int]()
        >>> A.inserir(5)
        >>> A.elementos()
        [5]

        Inserção de elemento repetido não altera o conjunto:

        >>> A.inserir(5)
        >>> A.elementos()
        [5]
        >>> A.tamanho()
        1

        Inserção em ordem crescente (exercita rotações da AVL):

        >>> B = Conjunto[int]()
        >>> for valor in range(1, 8):
        ...     B.inserir(valor)
        >>> B.elementos()
        [1, 2, 3, 4, 5, 6, 7]
        >>> B.tamanho()
        7
        """
        if not self.__arvore.buscar(x):
            self.__arvore.inserir(x)
            self.__tamanho += 1

    def remover(self, x: T) -> None:
        """
        Remove `x` do conjunto, caso pertença a ele.
        Se `x` não estiver presente, o conjunto não é modificado.

        Complexidade: O(log n). A busca e a remoção descem pela árvore, cuja
        altura é O(log n); o contador é O(1).

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.remover(2)
        >>> A.elementos()
        [1, 3]

        Remoção de elemento inexistente não altera o conjunto:

        >>> A.remover(99)
        >>> A.elementos()
        [1, 3]
        >>> A.tamanho()
        2

        Remoção em conjunto vazio:

        >>> Conjunto[int]().remover(1)

        Remover todos os elementos deixa o conjunto vazio:

        >>> A.remover(1)
        >>> A.remover(3)
        >>> A.vazio()
        True
        """
        if self.__arvore.buscar(x):
            self.__arvore.remover(x)
            self.__tamanho -= 1

    def contem(self, x: T) -> bool:
        """
        Retorna True se `x` pertence ao conjunto.

        Complexidade: O(log n). Cada comparação descarta uma subárvore, e a
        altura da AVL é O(log n).

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.contem(2)
        True
        >>> A.contem(7)
        False

        >>> Conjunto().contem(1)
        False
        """
        return self.__arvore.buscar(x)

    def tamanho(self) -> int:
        """
        Retorna a quantidade de elementos do conjunto.

        Complexidade: O(1), pois o tamanho fica guardado em `__tamanho`.

        Exemplos
        --------
        >>> Conjunto().tamanho()
        0

        >>> Conjunto([1, 2, 2, 3]).tamanho()
        3
        """
        return self.__tamanho

    def vazio(self) -> bool:
        """
        Retorna True se o conjunto não possui elementos.

        Complexidade: O(1), basta verificar se a raiz é None.

        Exemplos
        --------
        >>> Conjunto().vazio()
        True

        >>> Conjunto([1]).vazio()
        False
        """
        return self.__arvore.esta_vazia()

    def uniao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos de self, de `outro`
        ou de ambos. Não modifica self nem `outro`.

        Complexidade: O((n + m) log(n + m)). Copia self (n inserções) e insere os
        m elementos de `outro`, cada inserção em O(log(n + m)).

        Exemplos
        --------
        Parcialmente sobrepostos:

        >>> Conjunto([1, 2, 3, 4]).uniao(Conjunto([3, 4, 5, 6]))
        Conjunto([1, 2, 3, 4, 5, 6])

        Disjuntos:

        >>> Conjunto([1, 2]).uniao(Conjunto([3, 4]))
        Conjunto([1, 2, 3, 4])

        Iguais:

        >>> Conjunto([1, 2]).uniao(Conjunto([1, 2]))
        Conjunto([1, 2])

        Com vazio (nos dois lados):

        >>> Conjunto([1, 2]).uniao(Conjunto())
        Conjunto([1, 2])
        >>> Conjunto().uniao(Conjunto([1, 2]))
        Conjunto([1, 2])
        >>> Conjunto().uniao(Conjunto())
        Conjunto([])

        Os conjuntos de entrada não são modificados:

        >>> A = Conjunto([1, 2])
        >>> B = Conjunto([2, 3])
        >>> _ = A.uniao(B)
        >>> A, B
        (Conjunto([1, 2]), Conjunto([2, 3]))
        """
        resultado = Conjunto(self.elementos())
        for elemento in outro.elementos():
            resultado.inserir(elemento)
        return resultado

    def intersecao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos comuns a self e
        `outro`. Não modifica self nem `outro`.

        Complexidade: O(n log n + n log m). Percorre os n elementos de self; cada
        um é buscado em `outro` (O(log m)) e inserido no resultado (O(log n)).

        Exemplos
        --------
        Parcialmente sobrepostos:

        >>> Conjunto([1, 2, 3, 4]).intersecao(Conjunto([3, 4, 5, 6]))
        Conjunto([3, 4])

        Disjuntos:

        >>> Conjunto([1, 2]).intersecao(Conjunto([3, 4]))
        Conjunto([])

        Iguais:

        >>> Conjunto([1, 2]).intersecao(Conjunto([1, 2]))
        Conjunto([1, 2])

        Com vazio:

        >>> Conjunto([1, 2]).intersecao(Conjunto())
        Conjunto([])
        >>> Conjunto().intersecao(Conjunto([1, 2]))
        Conjunto([])

        Os conjuntos de entrada não são modificados:

        >>> A = Conjunto([1, 2, 3])
        >>> B = Conjunto([2, 3, 4])
        >>> _ = A.intersecao(B)
        >>> A, B
        (Conjunto([1, 2, 3]), Conjunto([2, 3, 4]))
        """
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if outro.contem(elemento):
                resultado.inserir(elemento)
        return resultado

    def diferenca(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos de self que não
        pertencem a `outro`. Não modifica self nem `outro`.

        A operação não é comutativa: A - B pode diferir de B - A.

        Complexidade: O(n log n + n log m). Percorre os n elementos de self; cada
        um é buscado em `outro` (O(log m)) e inserido no resultado (O(log n)).

        Exemplos
        --------
        Parcialmente sobrepostos:

        >>> Conjunto([1, 2, 3, 4]).diferenca(Conjunto([3, 4, 5, 6]))
        Conjunto([1, 2])
        >>> Conjunto([3, 4, 5, 6]).diferenca(Conjunto([1, 2, 3, 4]))
        Conjunto([5, 6])

        Disjuntos:

        >>> Conjunto([1, 2]).diferenca(Conjunto([3, 4]))
        Conjunto([1, 2])

        Iguais:

        >>> Conjunto([1, 2]).diferenca(Conjunto([1, 2]))
        Conjunto([])

        Com vazio:

        >>> Conjunto([1, 2]).diferenca(Conjunto())
        Conjunto([1, 2])
        >>> Conjunto().diferenca(Conjunto([1, 2]))
        Conjunto([])

        Os conjuntos de entrada não são modificados:

        >>> A = Conjunto([1, 2, 3])
        >>> B = Conjunto([3])
        >>> _ = A.diferenca(B)
        >>> A, B
        (Conjunto([1, 2, 3]), Conjunto([3]))
        """
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if not outro.contem(elemento):
                resultado.inserir(elemento)
        return resultado

    def contido(self, outro: Conjunto[T]) -> bool:
        """
        Retorna True se self é subconjunto de `outro`.

        Complexidade: O(n log m) no pior caso (n <= m): n buscas em `outro`.
        Se n > m, responde False em O(1) sem percorrer nada.

        Exemplos
        --------
        >>> Conjunto([1, 2]).contido(Conjunto([1, 2, 3]))
        True

        Todo conjunto está contido em si mesmo e o vazio está contido
        em qualquer conjunto:

        >>> Conjunto([1, 2]).contido(Conjunto([1, 2]))
        True
        >>> Conjunto().contido(Conjunto([1]))
        True

        >>> Conjunto([1, 4]).contido(Conjunto([1, 2, 3]))
        False
        >>> Conjunto([1, 2, 3]).contido(Conjunto([1, 2]))
        False
        """
        if self.tamanho() > outro.tamanho():
            return False

        for elemento in self.elementos():
            if not outro.contem(elemento):
                return False

        return True

    def __repr__(self) -> str:
        """
        Complexidade: O(n log n), por causa de elementos().

        >>> Conjunto([2, 1])
        Conjunto([1, 2])
        """
        return f"Conjunto({self.elementos()})"