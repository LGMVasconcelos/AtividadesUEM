from typing import Generic, TypeVar

from arranjo import Arranjo


T = TypeVar("T")


class Fila(Generic[T]):
    """
    Representa uma Fila implementada utilizando um arranjo estático.

    A Fila segue o princípio FIFO (First In, First Out): o primeiro
    elemento inserido é o primeiro elemento que pode ser removido.

    A representação utiliza o arranjo de forma circular.
    """

    __dados: Arranjo[T]
    __frente: int
    __fim: int
    __quantidade: int

    def __init__(self, capacidade: int) -> None:
        """
        Cria uma Fila vazia com a capacidade informada.

        Parâmetros
        ----------
        capacidade
        Número máximo de elementos que a Fila pode armazenar.

        Pré-condição
        ------------
        ``capacidade > 0``

        Pós-condição
        ------------
        A Fila está vazia e possui a capacidade informada.

        Exemplos
        --------
        >>> f = Fila[int](5)
        >>> f.is_empty()
        True
        >>> f.is_full()
        False
        """
        self.__dados = Arranjo[T](capacidade)
        self.__frente = 0
        self.__fim = 0
        self.__quantidade = 0

    def is_empty(self) -> bool:
        """
        Verifica se a Fila está vazia.

        Retorna
        -------
        bool
        ``True`` se a Fila estiver vazia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Fila permanece inalterado.

        Exemplos
        --------
        >>> f = Fila[int](3)
        >>> f.is_empty()
        True

        >>> f.enqueue(10)
        >>> f.is_empty()
        False
        """
        return self.__quantidade == 0

    def is_full(self) -> bool:
        """
        Verifica se a Fila está cheia.

        Retorna
        -------
        bool
        ``True`` se a Fila estiver cheia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Fila permanece inalterado.

        Exemplos
        --------
        >>> f = Fila[int](2)
        >>> f.is_full()
        False

        >>> f.enqueue(10)
        >>> f.enqueue(20)
        >>> f.is_full()
        True
        """
        return len(self.__dados) == self.__quantidade

    def enqueue(self, elemento: T) -> None:
        """
        Insere ``elemento`` no final da Fila.

        Parâmetros
        ----------
        elemento
        Elemento a ser inserido.

        Pré-condição
        ------------
        A Fila não está cheia.

        Pós-condição
        ------------
        ``elemento`` passa a ser o último elemento da Fila.
        A quantidade de elementos aumenta em uma unidade.

        Levanta
        -------
        OverflowError
        Se a Fila estiver cheia.

        Exemplos
        --------
        >>> f = Fila[str](3)
        >>> f.enqueue("A")
        >>> f.enqueue("B")
        >>> f.front()
        'A'

        >>> f.enqueue("C")
        >>> f.is_full()
        True

        >>> f.enqueue("D")
        Traceback (most recent call last):
        ...
        OverflowError: fila cheia
        """
        if self.is_full():
            raise OverflowError('fila cheia')
        
        self.__dados[self.__fim] = elemento
        self.__quantidade += 1
        self.__fim = (self.__fim + 1) % len(self.__dados)

    def dequeue(self) -> T:
        """
        Remove e retorna o primeiro elemento da Fila.

        Retorna
        -------
        T
        Elemento removido.

        Pré-condição
        ------------
        A Fila não está vazia.

        Pós-condição
        ------------
        O primeiro elemento é removido.
        A quantidade de elementos diminui em uma unidade.

        Levanta
        -------
        IndexError
        Se a Fila estiver vazia.

        Exemplos
        --------
        >>> f = Fila[int](3)
        >>> f.enqueue(10)
        >>> f.enqueue(20)
        >>> f.dequeue()
        10
        >>> f.dequeue()
        20
        >>> f.is_empty()
        True

        >>> f.dequeue()
        Traceback (most recent call last):
        ...
        IndexError: fila vazia
        """
        if self.is_empty():
            raise IndexError('fila vazia')
        
        dado = self.__dados[self.__frente]
        self.__frente = (self.__frente + 1) % len(self.__dados)
        self.__quantidade -= 1
        return dado

    def front(self) -> T:
        """
        Retorna o primeiro elemento da Fila sem removê-lo.

        Retorna
        -------
        T
        Elemento que está na frente da Fila.

        Pré-condição
        ------------
        A Fila não está vazia.

        Pós-condição
        ------------
        O estado da Fila permanece inalterado.

        Levanta
        -------
        IndexError
        Se a Fila estiver vazia.

        Exemplos
        --------
        >>> f = Fila[int](3)
        >>> f.enqueue(10)
        >>> f.enqueue(20)
        >>> f.front()
        10
        >>> f.front()
        10
        >>> f.dequeue()
        10

        >>> f = Fila[int](3)
        >>> f.front()
        Traceback (most recent call last):
        ...
        IndexError: fila vazia
        """
        if self.is_empty():
            raise IndexError('fila vazia')
        
        return self.__dados[self.__frente]
