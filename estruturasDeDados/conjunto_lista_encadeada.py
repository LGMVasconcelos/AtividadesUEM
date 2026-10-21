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

    def elementos(self) -> list[T]:
        """
        Retorna uma lista com todos os elementos do conjunto.

        Retorna
        -------
        list[T]
            Lista com todos os elementos do conjunto.

        Pós-condição
        ------------
        O estado do conjunto permanece inalterado.

        Exemplos
        --------
        >>> A = Conjunto([3, 1, 2])
        >>> A.elementos()
        [1, 2, 3]
        """

        for i in range(1, self.__lista.__len__()):
            chave = self.__lista[i]
            j = i - 1
            while j >= 0 and self.__lista[j] > chave:
                self.__lista[j + 1] = self.__lista[j]
                j -= 1
            self.__lista[j + 1] = chave
        return self.__lista

    def inserir(self, x: T) -> None:
            """
            Insere `x` no conjunto, caso ainda não pertença a ele.
            Se `x` já estiver presente, o conjunto não é modificado.
    
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
            if not self.__lista.find(x):
                self.__lista.insert(x)
                self.__tamanho += 1

    def remover(self, x: T) -> None:
        """
        Remove `x` do conjunto, caso pertença a ele.
        Se `x` não estiver presente, o conjunto não é modificado.

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.remover(2)
        >>> A.elementos()
        [1, 3]

        Remoção de elemento ausente não altera o conjunto:

        >>> A.remover(4)
        >>> A.elementos()
        [1, 3]
        >>> A.tamanho()
        2
        """
        if self.__lista.find(x):
            self.__lista.remove(x)
            self.__tamanho -= 1


    def contem(self, x: T) -> bool:
        """
        Verifica se `x` pertence ao conjunto.

        Retorna
        -------
        bool
            True se `x` pertence ao conjunto, False caso contrário.

        Pós-condição
        ------------
        O estado do conjunto permanece inalterado.

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.contem(2)
        True
        >>> A.contem(4)
        False
        """
        for i in range(self.__lista.__len__()):
            if self.__lista[i] == x:
                return True
        return False

    def tamanho(self) -> int:
        """
        Retorna o número de elementos do conjunto.

        Retorna
        -------
        int
            Número de elementos do conjunto.

        Pós-condição
        ------------
        O estado do conjunto permanece inalterado.

        Exemplos
        --------
        >>> A = Conjunto([1, 2, 3])
        >>> A.tamanho()
        3
        >>> B = Conjunto()
        >>> B.tamanho()
        0
        """
        return self.__tamanho

    def vazio(self) -> bool:
        """
        Verifica se o conjunto está vazio.

        Retorna
        -------
        bool
            True se o conjunto não possui elementos, False caso contrário.

        Pós-condição
        ------------
        O estado do conjunto permanece inalterado.

        Exemplos
        --------
        >>> A = Conjunto()
        >>> A.vazio()
        True
        >>> B = Conjunto([1])
        >>> B.vazio()
        False
        """
        return self.__lista.is_empty()

    def uniao(self, outro: Conjunto[T]) -> Conjunto[T]:
            """
            Retorna um novo conjunto com os elementos de self, de `outro`
            ou de ambos. Não modifica self nem `outro`.
    
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
            `outro`. Não modifica self nem `outro`.
    
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
            pertencem a `outro`. Não modifica self nem `outro`.
    
            A operação não é comutativa: A - B pode diferir de B - A.
    
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