from __future__ import annotations

from typing import Generic, Iterator, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    """
    Nó de uma lista ligada.

    Cada nó armazena um elemento do tipo T e uma referência para o
    próximo nó.

    ATENÇÃO:
        A classe Node deve ser utilizada para implementar a LinkedList.
        Não utilize a classe `list` do Python.
    """

    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] | None = None


class LinkedList(Generic[T]):
    """
    Estrutura de dados de lista ligada simples.

    A implementação da lista deve utilizar a classe Node definida acima.

    ATENÇÃO:
        Não utilize a classe `list` do Python para implementar a lista.

        Cada elemento da lista deve ser armazenado em um objeto Node.
        A lista deve manter uma referência para o primeiro nó (head)
        e a quantidade de elementos (_size).
    """

    def __init__(self):
        """
        Inicializa uma lista vazia.

        A implementação deve utilizar a classe Node.

        Não utilize `list` do Python.
        """
        self.__inicio = None
        self.__quantidade = 0

    def add(self, data: T) -> None:
        """
        Adiciona um elemento ao final da lista.

        Args:
            data: Elemento a ser adicionado.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.get(1)
            20
        """
        novo_no = Node(data)
        if self.__inicio is None:
            self.__inicio = novo_no
        else:
            atual = self.__inicio
            while atual.next is not None:
                atual = atual.next
            atual.next = novo_no
        self.__quantidade += 1

    def remove(self, index: int) -> T:
        """
        Remove e retorna o elemento de uma posição.

        Args:
            index: Índice do elemento.

        Returns:
            O elemento removido.

        Raises:
            IndexError: Se o índice for inválido.

        Exemplos:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> lista.remove(1)
            20
            >>> lista.get(1)
            30

            >>> lista.remove(0)
            10
        """
        if self.__quantidade == 0:
            raise IndexError("Lista vazia")

        if index < 0 or index >= self.__quantidade:
            raise IndexError("Índice inválido")

        if index == 0:
            data = self.__inicio.data
            self.__inicio = self.__inicio.next
        else:
            atual = self.__inicio
            for _ in range(index - 1):
                atual = atual.next
            data = atual.next.data
            atual.next = atual.next.next

        self.__quantidade -= 1
        return data

    def get(self, index: int) -> T:
        """
        Retorna o elemento de uma posição sem removê-lo.

        Args:
            index: Índice do elemento.

        Returns:
            O elemento encontrado.

        Raises:
            IndexError: Se o índice for inválido.

        Exemplos:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.get(0)
            10
            >>> lista.get(1)
            20
        """
        if self.__quantidade == 0:
            raise IndexError("Lista vazia")

        if index < 0 or index >= self.__quantidade:
            raise IndexError("Índice inválido")

        atual = self.__inicio
        for _ in range(index):
            atual = atual.next
        return atual.data

    def find(self, data: T) -> int:
        """
        Devolve o índice do elemento na lista, ou -1 caso não encontre.

        Args:
            data: Elemento a ser procurado.

        Returns:
            O índice da primeira ocorrência do elemento ou -1 caso o
            elemento não esteja na lista.

        Exemplos:
            >>> lista = LinkedList[str]()
            >>> lista.add("a")
            >>> lista.add("b")
            >>> lista.add("c")
            >>> lista.find("b")
            1
            >>> lista.find("x")
            -1
        """
        atual = self.__inicio
        index = 0
        while atual is not None:
            if atual.data == data:
                return index
            atual = atual.next
            index += 1
        return -1

    def size(self) -> int:
        """
        Retorna a quantidade de elementos.

        Returns:
            Número de elementos.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.size()
            2
        """
        return self.__quantidade

    def is_empty(self) -> bool:
        """
        Verifica se a lista está vazia.

        Returns:
            True se estiver vazia; False caso contrário.

        Exemplos:
            >>> lista = LinkedList[int]()
            >>> lista.is_empty()
            True
            >>> lista.add(10)
            >>> lista.is_empty()
            False
        """
        return self.__quantidade == 0

    def __len__(self) -> int:
        """
        Retorna a quantidade de elementos.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> len(lista)
            2
        """
        return self.__quantidade

    def __iter__(self) -> Iterator[T]:
        """
        Permite percorrer a lista com for.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> list(lista)
            [10, 20, 30]
        """
        atual = self.__inicio
        while atual is not None:
            yield atual.data
            atual = atual.next

