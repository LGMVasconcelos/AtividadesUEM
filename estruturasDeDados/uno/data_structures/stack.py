from typing import Generic, TypeVar

from arranjo import Arranjo

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Estrutura de dados do tipo Pilha (LIFO).

    O último elemento inserido é o primeiro a ser removido.

    ATENÇÃO:
        Não utilize a classe `list` do Python para implementar a pilha.

        A estrutura deve ser implementada utilizando a classe Arranjo
        (implementação de arranjo estático) ou encadeamento.

        A Stack não deve ter uma capacidade máxima. Ela deve poder
        crescer conforme novos elementos forem inseridos.
    """

    __dados: Arranjo[T]
    __topo: int

    def __init__(self) -> None:
        """
        Inicializa uma pilha vazia.

        A estrutura interna deve ser implementada utilizando a classe
        Arranjo ou a encadeamento.

        Não utilize `list` do Python.

        A Stack não deve possuir uma capacidade máxima.
        """
        self.__dados = Arranjo[T](1)
        self.__topo = -1

    def push(self, item: T) -> None:
        """
        Adiciona um elemento ao topo da pilha.

        Args:
            item: Elemento a ser adicionado.

        Exemplo:
            >>> stack = Stack[int]()
            >>> stack.push(10)
            >>> stack.push(20)
            >>> stack.peek()
            20
        """
        if self.__topo + 1 == len(self.__dados):
            novo_arranjo = Arranjo[T](len(self.__dados) * 2)
            for i in range(len(self.__dados)):
                novo_arranjo[i] = self.__dados[i]
            self.__dados = novo_arranjo

        self.__topo += 1
        self.__dados[self.__topo] = item

    def pop(self) -> T:
        """
        Remove e retorna o elemento do topo.

        Returns:
            O elemento removido.

        Raises:
            IndexError: Se a pilha estiver vazia.

        Exemplo:
            >>> stack = Stack[str]()
            >>> stack.push("a")
            >>> stack.push("b")
            >>> stack.pop()
            'b'
            >>> stack.pop()
            'a'
        """
        if self.is_empty():
            raise IndexError("pilha vazia")

        elemento = self.__dados[self.__topo]
        self.__topo -= 1
        return elemento

    def peek(self) -> T:
        """
        Retorna o elemento do topo sem removê-lo.

        Returns:
            O elemento no topo da pilha.

        Raises:
            IndexError: Se a pilha estiver vazia.

        Exemplo:
            >>> stack = Stack[int]()
            >>> stack.push(10)
            >>> stack.push(20)
            >>> stack.peek()
            20
        """
        if self.is_empty():
            raise IndexError("pilha vazia")
        return self.__dados[self.__topo]

    def is_empty(self) -> bool:
        """
        Verifica se a pilha está vazia.

        Returns:
            True se estiver vazia; False caso contrário.

        Exemplo:
            >>> stack = Stack[int]()
            >>> stack.is_empty()
            True
            >>> stack.push(1)
            >>> stack.is_empty()
            False
        """
        return self.__topo == -1

    def size(self) -> int:
        """
        Retorna a quantidade de elementos.

        Returns:
            Número de elementos da pilha.

        Exemplo:
            >>> stack = Stack[int]()
            >>> stack.size()
            0
            >>> stack.push(10)
            >>> stack.push(20)
            >>> stack.size()
            2
        """
        return self.__topo + 1

    def __len__(self) -> int:
        """
        Retorna a quantidade de elementos da pilha.

        Exemplo:
            >>> stack = Stack[int]()
            >>> stack.push(10)
            >>> stack.push(20)
            >>> len(stack)
            2
        """
        return self.__topo + 1
