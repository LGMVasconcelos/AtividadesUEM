from __future__ import annotations
from typing import Generic, TypeVar

from dataclasses import dataclass

T = TypeVar("T")

@dataclass
class No(Generic[T]):
    elemento: T
    proximo: No[T] | None




class ListaEncadeada(Generic[T]):
    """
    Representa uma Lista implementada utilizando encadeamento.

    A Lista representa uma sequência ordenada de elementos, permitindo
    acesso, alteração, busca, inserção e remoção em diferentes posições.

    A representação utiliza um arranjo cuja capacidade pode ser aumentada
    quando necessário.
    """

    __inicio: No[T] | None
    __quantidade: int

    def __init__(self) -> None:
        """
        Cria uma Lista vazia.

        Pós-condição
        ------------
        A Lista está vazia.

        Exemplos
        --------
        >>> lista = ListaEncadeada[int]()
        >>> lista.is_empty()
        True
        >>> len(lista)
        0
        """
        self.__inicio = None
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
        >>> lista = ListaEncadeada[int]()
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
        >>> lista = ListaEncadeada[int]()
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
        ``0 <= posição < size()``

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = ListaEncadeada[int]()
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
            raise IndexError('posição inválida')

        if self.is_empty():
            raise ValueError('lista vazia')

        p: No[T] | None = self.__inicio
        for i in range(0, posição):
            p = p.proximo
        return p.elemento


    def __setitem__(self, posição: int, elemento: T) -> None:
        """
        Substitui o elemento armazenado na posição informada.

        Parâmetros
        ----------
        posição
            Posição do elemento que será substituído.
        elemento
            Novo elemento.

        Pré-condição
        ------------
        ``0 <= posição < size()``

        Pós-condição
        ------------
        O elemento na posição informada foi substituído.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = ListaEncadeada[int]()
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista[1] = 25
        >>> lista[1]
        25
        """
        if posição < 0 or posição >= self.__quantidade:
            raise IndexError('posição inválida')

        if self.is_empty():
            raise ValueError('lista vazia')

        p: No[T] | None = self.__inicio
        for i in range(0, posição):
            p = p.proximo
        p.elemento = elemento
        

    def find(self, elemento: T) -> int:
        """
        Procura um elemento na Lista.

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
        >>> lista = ListaEncadeada[int]()
        >>> lista.insert(0, 10)
        >>> lista.insert(1, 20)
        >>> lista.insert(2, 30)
        >>> lista.find(20)
        1
        >>> lista.find(50)
        -1
        """
        p = self.__inicio
        i = 0
        while p != None: 
            if p.elemento == elemento:
                return i
            i += 1
            p = p.proximo
        return -1


    def insert(self, posição: int, elemento: T) -> None:
        """
        Insere um elemento na posição informada.

        Os elementos a partir da posição de inserção são deslocados
        uma posição para a direita.

        Parâmetros
        ----------
        posição
            Posição na qual o elemento será inserido.
        elemento
            Elemento a ser inserido.

        Pré-condição
        ------------
        ``0 <= posição <= size()``

        Pós-condição
        ------------
        O elemento passa a ocupar a posição informada.
        A quantidade de elementos aumenta em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = ListaEncadeada[str]()
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
            raise IndexError('posição inválida')

        novo = No(elemento, None)

        if self.__inicio == None:
            self.__inicio = novo
        else:
            if posição == 0:
                novo.proximo = self.__inicio
                self.__inicio = novo
            else:
                p: No[T] | None = self.__inicio
                for i in range(0, posição-1):
                    p = p.proximo
                novo.proximo = p.proximo
                p.proximo = novo
        self.__quantidade += 1
        

    def remove(self, posição: int) -> T:
        """
        Remove e retorna o elemento da posição informada.

        Os elementos posteriores à posição são deslocados
        uma posição para a esquerda.

        Parâmetros
        ----------
        posição
            Posição do elemento que será removido.

        Retorna
        -------
        T
            Elemento removido.

        Pré-condição
        ------------
        ``0 <= posição < size()``

        Pós-condição
        ------------
        O elemento da posição informada foi removido.
        A quantidade de elementos diminui em uma unidade.

        Levanta
        -------
        IndexError
            Se a posição for inválida.

        Exemplos
        --------
        >>> lista = ListaEncadeada[str]()
        >>> lista.insert(0, "A")
        >>> lista.insert(1, "B")
        >>> lista.insert(2, "C")
        >>> lista.remove(1)
        'B'
        >>> lista[0]
        'A'
        >>> lista[1]
        'C'

        >>> lista.remove(2)
        Traceback (most recent call last):
        ...
        IndexError: posição inválida
        """
        if posição < 0 or posição >= self.__quantidade:
            raise IndexError('posição inválida')

        if posição == 0:
            self.__inicio = self.__inicio.proximo
        else:
            p: No[T] | None = self.__inicio
            for i in range(0, posição-1):
                p = p.proximo
            elemento = p.proximo.elemento
            p.proximo = p.proximo.proximo

        self.__quantidade -= 1
        return elemento