from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class No(Generic[T]):
    """
    Representa um nó de uma lista duplamente encadeada circular.

    Cada nó armazena um elemento e referências para os nós anterior
    e seguinte na sequência.

    Em uma lista não vazia, as referências formam um ciclo: o próximo
    nó do último nó é o primeiro nó da lista, e o nó anterior ao
    primeiro nó é o último nó.

    Parâmetros
    ----------
    elemento
        Elemento armazenado no nó.
    proximo
        Referência para o próximo nó da lista.
    anterior
        Referência para o nó anterior da lista.
    """
    elemento: T | None = None
    proximo: No[T] | None = None
    anterior: No[T] | None = None


class Lista(Generic[T]):
    """
    Representa uma lista duplamente encadeada circular.

    A Lista representa uma sequência ordenada de elementos, permitindo
    acesso, alteração, busca, inserção e remoção em diferentes posições.

    A representação utiliza nós duplamente encadeados. Cada nó armazena
    um elemento e referências para os nós anterior e seguinte.

    Os nós formam uma estrutura circular. Em uma lista não vazia, o
    próximo nó do último nó é o primeiro nó, e o nó anterior ao primeiro
    nó é o último nó.

    A Lista mantém uma referência para o primeiro nó e a quantidade
    de elementos armazenados.
    """

    __sentinela: No[T]
    __quantidade: int

    def __init__(self) -> None:
        """
        Cria uma Lista vazia.

        Pós-condição
        ------------
        A Lista está vazia.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> lista.is_empty()
        True
        >>> len(lista)
        0
        """
        self.__sentinela = No()
        self.__sentinela.proximo = self.__sentinela
        self.__sentinela.anterior = self.__sentinela
        self.__quantidade = 0

    def __len__(self) -> int:
        """
        Retorna a quantidade de elementos da Lista.

        Retorna
        -------
        int
            Número de elementos armazenados na Lista.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> len(lista)
        0

        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> len(lista)
        2
        """
        return self.__quantidade

    def is_empty(self) -> bool:
        """
        Verifica se a Lista está vazia.

        Retorna
        -------
        bool
            ``True`` se a Lista estiver vazia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> lista.is_empty()
        True

        >>> lista.insert(0, 10)
        >>> lista.is_empty()
        False
        """
        return self.__quantidade == 0

    def __getitem__(self, posição: int) -> T:
        """
        Retorna o elemento armazenado na posição informada.

        O percurso começa no primeiro nó e segue pelas referências
        ``proximo`` até alcançar a posição solicitada. Como a lista é
        circular, o percurso é limitado pela posição solicitada e não
        depende de uma referência ``None`` para identificar o final.

        Parâmetros
        ----------
        posição
            Posição do elemento na Lista.

        Retorna
        -------
        T
            Elemento armazenado na posição.

        Pré-condição
        ------------
        ``0 <= posição < len(lista)``

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista.insert(2, 30)
        >>> lista[1]
        20

        >>> lista[3]
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        if posição < 0 or posição >= self.__quantidade:
            raise IndexError("posição inválida")

        p = self.__sentinela.proximo
        for _ in range(posição):
            p = p.proximo

        return p.elemento

    def __setitem__(self, posição: int, elemento: T) -> None:
        """
        Substitui o elemento armazenado na posição informada.

        O nó correspondente à posição é localizado percorrendo a lista
        a partir do primeiro nó por meio das referências ``proximo``.

        Parâmetros
        ----------
        posição
            Posição do elemento que será substituído.
        elemento
            Novo elemento.

        Pré-condição
        ------------
        ``0 <= posição < len(lista)``

        Pós-condição
        ------------
        O elemento armazenado no nó da posição informada foi substituído.
        A estrutura de encadeamento da lista permanece inalterada.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista[1] = 25
        >>> lista[1]
        25
        """
        if posição < 0 or posição >= self.__quantidade:
            raise IndexError("posição inválida")

        p = self.__sentinela.proximo
        for _ in range(posição):
            p = p.proximo

        p.elemento = elemento

    def find(self, elemento: T) -> int:
        """
        Procura um elemento na Lista.

        A busca começa no primeiro nó e percorre a lista por meio das
        referências ``proximo``. Como a lista é circular, o percurso é
        limitado pela quantidade de elementos para evitar percorrer o
        ciclo indefinidamente.

        Parâmetros
        ----------
        elemento
            Elemento procurado.

        Retorna
        -------
        int
            Posição da primeira ocorrência do elemento.
            Retorna ``-1`` se o elemento não estiver na Lista.

        Pós-condição
        ------------
        O estado da Lista permanece inalterado.

        Exemplos
        --------
        >>> lista = Lista[int]()
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista.insert(2, 30)

        >>> lista.find(10)
        0
        >>> lista.find(20)
        1
        >>> lista.find(30)
        2
        >>> lista.find(50)
        -1
        """
        p = self.__sentinela.proximo

        for posição in range(self.__quantidade):
            if p.elemento == elemento:
                return posição

            p = p.proximo

        return -1

    def insert(self, posição: int, elemento: T) -> None:
        """
        Insere um elemento na posição informada.

        A inserção cria um novo nó e ajusta as referências ``proximo``
        e ``anterior`` dos nós envolvidos, preservando o encadeamento
        duplo e circular da lista.

        Quando a posição é zero, o novo nó passa a ser o primeiro da
        Lista. Nesse caso, ele é ligado ao antigo primeiro nó e ao
        último nó.

        Nas demais posições, o novo nó é inserido entre o nó anterior
        à posição e o nó que ocupava essa posição.

        Se a lista estiver vazia, o novo nó referencia a si próprio
        tanto por ``proximo`` quanto por ``anterior``.

        Parâmetros
        ----------
        posição
            Posição na qual o elemento será inserido.
        elemento
            Elemento a ser inserido.

        Pré-condição
        ------------
        ``0 <= posição <= len(lista)``

        Pós-condição
        ------------
        Um novo nó contendo o elemento passa a ocupar a posição
        informada, as referências ``proximo`` e ``anterior`` permanecem
        consistentes e a quantidade de elementos aumenta em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[str]()
        >>> lista.insert(0, "A")
        >>> lista.insert(1, "B")
        >>> lista.insert(2, "D")
        >>> lista.insert(2, "C")
        >>> lista[0]
        'A'
        >>> lista[1]
        'B'
        >>> lista[2]
        'C'
        >>> lista[3]
        'D'

        >>> lista.insert(5, "X")
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        if posição < 0 or posição > self.__quantidade:
            raise IndexError("posição inválida")

        novo = No(elemento)

        p = self.__sentinela

        for _ in range(posição):
            p = p.proximo

        novo.anterior = p
        novo.proximo = p.proximo
        p.proximo.anterior = novo
        p.proximo = novo

        self.__quantidade += 1

    def remove(self, posição: int) -> T:
        """
        Remove e retorna o elemento da posição informada.

        A remoção ajusta as referências ``proximo`` e ``anterior`` dos
        nós adjacentes ao nó removido, preservando o encadeamento duplo
        e circular da lista.

        Quando a lista possui apenas um nó, esse nó é removido e a lista
        passa a ficar vazia.

        Quando a posição é zero, o primeiro nó é removido, o segundo nó
        passa a ser o primeiro e as referências do primeiro e do último
        nó são atualizadas para preservar a circularidade.

        Nas demais posições, o nó anterior ao removido passa a apontar
        para o nó seguinte, e o nó seguinte passa a apontar para o nó
        anterior.

        Parâmetros
        ----------
        posição
            Posição do elemento que será removido.

        Retorna
        -------
        T
            Elemento armazenado no nó removido.

        Pré-condição
        ------------
        ``0 <= posição < len(lista)``

        Pós-condição
        ------------
        O nó da posição informada foi removido do encadeamento,
        a circularidade da lista foi preservada e a quantidade de
        elementos diminui em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = Lista[str]()
        >>> lista.insert(0, "A")
        >>> lista.insert(1, "B")
        >>> lista.insert(2, "C")
        >>> lista.remove(1)
        'B'
        >>> lista[0]
        'A'
        >>> lista[1]
        'C'

        >>> lista.remove(0)
        'A'
        >>> lista[0]
        'C'

        >>> lista.remove(1)
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        if posição < 0 or posição >= self.__quantidade:
            raise IndexError("posição inválida")

        p = self.__sentinela

        for _ in range(posição):
            p = p.proximo

        removido = p.proximo
        elemento = removido.elemento
        p.proximo = removido.proximo
        removido.proximo.anterior = p

        self.__quantidade -= 1
        return elemento



    def inverte_lista(self) -> None:
        if self.is_empty() or self.__quantidade == 1:
            return

        p = self.__sentinela
        for _ in range(self.__quantidade + 1):
            aux = p.proximo
            p.proximo = p.anterior
            p.anterior = aux
            p = p.anterior

    def insere_ordenado(self, elemento: T) -> None:
        p = self.__sentinela.proximo
        posição = 0

        while p != self.__sentinela and p.elemento < elemento:
            p = p.proximo
            posição += 1

        self.insert(posição, elemento)

    def __str__(self) -> str:
        elementos = []
        p = self.__sentinela.proximo

        for _ in range(self.__quantidade):
            elementos.append(str(p.elemento))
            p = p.proximo

        return ", ".join(elementos)


lista = Lista[int]()
lista.insert(0, 10)
lista.insert(1, 20)
lista.insert(2, 30)
lista.insert(3, 40)
print("Lista original:", str(lista))
lista.insere_ordenado(25)
print("Lista após inserção ordenada de 25:", str(lista))
lista.inverte_lista()
print("Lista invertida:", str(lista))
