from __future__ import annotations

from typing import Generic, TypeVar

from lista_encadeada import ListaEncadeada

T = TypeVar("T")


class Conjunto(Generic[T]):
    """
    Tipo Abstrato de Dados Conjunto: coleção de elementos distintos,
    sem repetições e sem noção de posição.

    Representação: lista simplesmente encadeada (ver lista_encadeada.py),
    sem ordenação.

    Invariantes
    -----------
    - A lista nunca contém elementos duplicados (comparados com ==).
    - O tamanho do conjunto é sempre o tamanho da lista.

    Pré-requisito geral
    -------------------

    Operações que produzem novos conjuntos (uniao, intersecao, diferenca)
    NÃO modificam os conjuntos de entrada.

    A ordem dos elementos não faz parte da especificação: ``elementos()``
    pode devolvê-los em qualquer ordem. Por isso os testes comparam
    conjuntos com ``==`` ou usam ``sorted``.

    Complexidade
    ------------
    Nas operações abaixo, n = tamanho de self e m = tamanho de `outro`.

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
        Elementos repetidos são ignorados. Sem argumentos, cria um
        conjunto vazio (operação ``criar()`` da especificação).

        Parâmetros
        ----------
        elementos_iniciais
            Elementos que formam o conjunto. Pode ter repetições.

        Pós-condição
        ------------
        O conjunto contém exatamente os elementos distintos de
        `elementos_iniciais`. A lista recebida não é modificada.

        Exemplos
        --------
        >>> Conjunto()
        Conjunto([])

        >>> Conjunto([3, 1, 3, 2, 1])
        Conjunto([1, 2, 3])
        """
        self.__lista: ListaEncadeada[T] = ListaEncadeada()
        if elementos_iniciais is not None:
            for elemento in elementos_iniciais:
                self.inserir(elemento)

    def elementos(self) -> list[T]:
        """
        Retorna uma nova lista Python com os elementos do conjunto,
        em ordem arbitrária.

        Retorna
        -------
        list[T]
            Cópia dos elementos, sem repetições.

        Pós-condição
        ------------
        O conjunto permanece inalterado. Alterar a lista retornada não
        altera o conjunto.

        Complexidade: O(n).

        Exemplos
        --------
        >>> sorted(Conjunto([3, 1, 2]).elementos())
        [1, 2, 3]

        >>> Conjunto().elementos()
        []

        A lista retornada é uma cópia:

        >>> A = Conjunto([1, 2])
        >>> A.elementos().clear()
        >>> A.tamanho()
        2
        """
        return self.__lista.to_list()

    def inserir(self, x: T) -> None:
        """
        Insere `x` no conjunto, caso ainda não pertença a ele.
        Se `x` já estiver presente, o conjunto não é modificado.

        Parâmetros
        ----------
        x
            Elemento a inserir.

        Pós-condição
        ------------
        `x` pertence ao conjunto. O tamanho aumenta em uma unidade se
        `x` era novo; caso contrário, permanece o mesmo.

        Complexidade: O(n), pela verificação de duplicata (a inserção
        em si, no início da lista, é O(1)).

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

        Inserção de vários elementos distintos:

        >>> B = Conjunto[int]()
        >>> for valor in range(1, 8):
        ...     B.inserir(valor)
        >>> sorted(B.elementos())
        [1, 2, 3, 4, 5, 6, 7]
        >>> B.tamanho()
        7
        """
        if not self.contem(x):
            self.__lista.insert(0, x)

    def remover(self, x: T) -> None:
        """
        Remove `x` do conjunto, caso pertença a ele.
        Se `x` não estiver presente, o conjunto não é modificado.

        Parâmetros
        ----------
        x
            Elemento a remover.

        Pós-condição
        ------------
        `x` não pertence ao conjunto. O tamanho diminui em uma unidade
        se `x` estava presente; caso contrário, permanece o mesmo.

        Complexidade: O(n), pela busca de `x` na lista.

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.remover(2)
        >>> sorted(A.elementos())
        [1, 3]

        Remoção de elemento inexistente não altera o conjunto:

        >>> A.remover(99)
        >>> sorted(A.elementos())
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
        posicao = self.__lista.find(x)
        if posicao != -1:
            self.__lista.remove(posicao)

    def contem(self, x: T) -> bool:
        """
        Verifica se `x` pertence ao conjunto.

        Parâmetros
        ----------
        x
            Elemento procurado.

        Retorna
        -------
        bool
            True se `x` pertence ao conjunto, False caso contrário.

        Pós-condição
        ------------
        O conjunto permanece inalterado.

        Complexidade: O(n), pois a lista pode ser percorrida inteira.

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
        return self.__lista.find(x) != -1

    def tamanho(self) -> int:
        """
        Retorna o número de elementos do conjunto.

        Retorna
        -------
        int
            Número de elementos distintos do conjunto.

        Pós-condição
        ------------
        O conjunto permanece inalterado.

        Complexidade: O(1), pois a lista mantém a quantidade.

        Exemplos
        --------
        >>> Conjunto().tamanho()
        0

        >>> Conjunto([1, 2, 2, 3]).tamanho()
        3
        """
        return len(self.__lista)

    def vazio(self) -> bool:
        """
        Verifica se o conjunto está vazio.

        Retorna
        -------
        bool
            True se o conjunto não possui elementos, False caso contrário.

        Pós-condição
        ------------
        O conjunto permanece inalterado.

        Complexidade: O(1).

        Exemplos
        --------
        >>> Conjunto().vazio()
        True

        >>> Conjunto([1]).vazio()
        False
        """
        return self.__lista.is_empty()

    def uniao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos de self, de `outro`
        ou de ambos.

        Parâmetros
        ----------
        outro
            Segundo conjunto da operação.

        Retorna
        -------
        Conjunto[T]
            Novo conjunto, independente de self e de `outro`.

        Pós-condição
        ------------
        self e `outro` permanecem inalterados.

        Complexidade: O((n + m)²), pois cada inserção verifica
        duplicata percorrendo a lista do resultado.

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
        >>> C = A.uniao(B)
        >>> A, B, C
        (Conjunto([1, 2]), Conjunto([2, 3]), Conjunto([1, 2, 3]))
        """
        resultado = Conjunto(self.elementos())
        for elemento in outro.elementos():
            resultado.inserir(elemento)
        return resultado

    def intersecao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos comuns a self e
        `outro`.

        Parâmetros
        ----------
        outro
            Segundo conjunto da operação.

        Retorna
        -------
        Conjunto[T]
            Novo conjunto, independente de self e de `outro`.

        Pós-condição
        ------------
        self e `outro` permanecem inalterados.

        Complexidade: O(n · m), pois cada elemento de self é buscado
        na lista de `outro`.

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
        >>> C = A.intersecao(B)
        >>> A, B, C
        (Conjunto([1, 2, 3]), Conjunto([2, 3, 4]), Conjunto([2, 3]))
        """
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if outro.contem(elemento):
                resultado.inserir(elemento)
        return resultado

    def diferenca(self, outro: Conjunto[T]) -> Conjunto[T]:
        """
        Retorna um novo conjunto com os elementos de self que não
        pertencem a `outro`.

        A operação não é comutativa: A - B pode diferir de B - A.

        Parâmetros
        ----------
        outro
            Conjunto cujos elementos são excluídos do resultado.

        Retorna
        -------
        Conjunto[T]
            Novo conjunto, independente de self e de `outro`.

        Pós-condição
        ------------
        self e `outro` permanecem inalterados.

        Complexidade: O(n · (n + m)): para cada elemento de self há
        uma busca em `outro` e uma inserção no resultado.

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
        >>> C = A.diferenca(B)
        >>> A, B, C
        (Conjunto([1, 2, 3]), Conjunto([3]), Conjunto([1, 2]))
        """
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if not outro.contem(elemento):
                resultado.inserir(elemento)
        return resultado

    def contido(self, outro: Conjunto[T]) -> bool:
        """
        Retorna True se self é subconjunto de `outro`.

        Parâmetros
        ----------
        outro
            Conjunto que se verifica conter self.

        Retorna
        -------
        bool
            True se todo elemento de self pertence a `outro`.

        Pós-condição
        ------------
        self e `outro` permanecem inalterados.

        Complexidade: O(n · m) no pior caso. Se n > m, a resposta
        False sai em O(1).

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
        >>> Conjunto().contido(Conjunto())
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

    def __elementos_ordenados(self) -> list[T]:
        """
        Retorna uma nova lista Python com os elementos em ordem
        crescente, usando insertion sort.
 
        Ordena uma cópia (obtida de `elementos()`); o conjunto e a
        lista encadeada interna não são modificados.
 
        Complexidade: O(n²) no pior caso.
 
        >>> Conjunto([3, 1, 2])._Conjunto__elementos_ordenados()
        [1, 2, 3]
        >>> Conjunto()._Conjunto__elementos_ordenados()
        []
        """
        v = self.elementos()
        for i in range(1, len(v)):
            chave = v[i]
            j = i - 1
            while j >= 0 and v[j] > chave:
                v[j + 1] = v[j]
                j -= 1
            v[j + 1] = chave
        return v
 
    def __repr__(self) -> str:
        """
        Representação textual, com os elementos em ordem crescente
        (para que a saída seja previsível nos testes).
 
        Complexidade: O(n²), pelo insertion sort.
 
        >>> Conjunto([2, 1])
        Conjunto([1, 2])
        """
        return f"Conjunto({self.__elementos_ordenados()})"