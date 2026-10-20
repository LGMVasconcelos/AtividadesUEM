from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass
class No(Generic[T]):
    """
    Representa um nó de uma árvore binária de busca.

    Cada nó armazena um valor, uma altura e possui referências para,
    no máximo, dois filhos: esquerdo e direito.
    """

    valor: T
    altura: int = 0
    esquerda: No[T] | None = None
    direita: No[T] | None = None


class AVL(Generic[T]):
    """
    Tipo abstrato de Dados Árvore AVL.

    A árvore mantém a seguinte propriedade para cada nó:

        valores da subárvore esquerda < valor do nó
        valores da subárvore direita > valor do nó

    Além disso, para cada nó, o fator de balanceamento deve
    pertencer ao intervalo [-1, 1].

    A AVL não permite valores duplicados."""

    def __init__(self) -> None:
        """
        Cria uma árvore AVL vazia.

        A árvore criada não contém elementos.
        """
        self.__raiz = None

    def esta_vazia(self) -> bool:
        """
        Verifica se a árvore está vazia.

        Retorna True se a árvore não possuir elementos e False
        caso contrário.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.esta_vazia()
        True

        >>> arvore.inserir(50)
        >>> arvore.esta_vazia()
        False
        """
        return self.__raiz is None

    def inserir(self, valor: T) -> None:
        """
        Insere `valor` na árvore, preservando a propriedade de AVL.

        Pré-requisito:
        `valor` deve ser comparável com os valores armazenados
        na árvore.

        Se `valor` já estiver presente, a árvore não é modificada.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.inserir(50)
        >>> arvore.inserir(30)
        >>> arvore.inserir(80)
        >>> arvore.em_ordem()
        [30, 50, 80]
        """
        self.__raiz = self.__inserir(self.__raiz, valor)
        
    def __inserir(self, atual: No[T]|None, valor: T) -> No[T]:
        """
        Insere recursivamente um valor e rebalanceia a subárvore.

        TODO:
        1. Tratar o caso-base de um nó vazio.
        2. Percorrer a árvore conforme a propriedade de AVL.
        3. Ignorar valores duplicados.
        4. Atualizar a altura do nó.
        5. Rebalancear a subárvore.
        6. Retornar a raiz atualizada da subárvore.
        """
        if atual is None:
            return No(valor)

        if atual.valor > valor:
            atual.esquerda = self.__inserir(atual.esquerda, valor)
        elif atual.valor < valor:
            atual.direita = self.__inserir(atual.direita, valor)

        return self.__rebalancear(atual)


    def buscar(self, valor: T) -> bool:
        """
        Verifica se `valor` está presente na árvore.

        Retorna True se o valor estiver armazenado e False caso
        contrário.

        Pré-requisito:
        `valor` deve ser comparável com os valores armazenados
        na árvore.

        A operação não modifica a árvore.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.inserir(50)
        >>> arvore.inserir(30)
        >>> arvore.inserir(80)

        >>> arvore.buscar(30)
        True

        >>> arvore.buscar(70)
        False
        """
        return self.__buscar(self.__raiz, valor)
    
    def __buscar(self, atual: No[T]|None, valor: T) -> bool:
        if atual is None:
            return False
        
        if atual.valor > valor:
            return self.__buscar(atual.esquerda, valor)
        
        if atual.valor < valor:
            return self.__buscar(atual.direita, valor)
        
        return True


    def pre_ordem(self) -> list[T]:
        """
        Retorna os valores da árvore em pré-ordem:
        raiz, subárvore esquerda, subárvore direita.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> for valor in [50, 30, 80, 20, 40, 70, 90]:
        ...     arvore.inserir(valor)

        >>> arvore.pre_ordem()
        [50, 30, 20, 40, 80, 70, 90]
        """
        return self.__pre_ordem(self.__raiz)
    
    def __pre_ordem(self, atual: No[T]|None) -> list[T]:
        if atual is None:
            return []
        return [atual.valor] + self.__pre_ordem(atual.esquerda) + self.__pre_ordem(atual.direita)


    def em_ordem(self) -> list[T]:
        """
        Retorna os valores da árvore em ordem:
        subárvore esquerda, raiz, subárvore direita.

        Em uma AVL sem valores duplicados, os valores são
        retornados em ordem crescente.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> for valor in [50, 30, 80, 20, 40, 70, 90]:
        ...     arvore.inserir(valor)

        >>> arvore.em_ordem()
        [20, 30, 40, 50, 70, 80, 90]
        """
        return self.__em_ordem(self.__raiz)
    
    def __em_ordem(self, atual: No[T]|None) -> list[T]:
        if atual is None:
            return []
        return self.__em_ordem(atual.esquerda) + [atual.valor] + self.__em_ordem(atual.direita)



    def pos_ordem(self) -> list[T]:
        """
        Retorna os valores da árvore em pós-ordem:
        subárvore esquerda, subárvore direita, raiz.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> for valor in [50, 30, 80, 20, 40, 70, 90]:
        ...     arvore.inserir(valor)

        >>> arvore.pos_ordem()
        [20, 40, 30, 70, 90, 80, 50]
        """
        return self.__pos_ordem(self.__raiz)
    
    def __pos_ordem(self, atual: No[T]|None) -> list[T]:
        if atual is None:
            return []
        return self.__pos_ordem(atual.esquerda) + self.__pos_ordem(atual.direita) + [atual.valor] 


    def quantidade(self) -> int:
        """
        Retorna a quantidade de elementos armazenados na árvore.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.quantidade()
        0

        >>> for valor in [50, 30, 80]:
        ...     arvore.inserir(valor)

        >>> arvore.quantidade()
        3
        """
        return self.__quantidade(self.__raiz)
        

    def __quantidade(self, atual: No[T]|None) -> int:
        if atual is None:
            return 0
        return 1 + self.__quantidade(atual.esquerda) + self.__quantidade(atual.direita)


    def altura(self) -> int:
        """
        Retorna a altura da árvore.

        A raiz está no nível 0.

        Por essa definição:
            - árvore vazia possui altura -1;
            - árvore com apenas a raiz possui altura 0.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.altura()
        -1

        >>> arvore.inserir(50)
        >>> arvore.altura()
        0

        >>> for valor in [30, 80, 20, 40, 70, 90]:
        ...     arvore.inserir(valor)

        >>> arvore.altura()
        2
        """
        return self.__altura_no(self.__raiz)


    # ======================================================
    # AUXILIARES DE ALTURA E BALANCEAMENTO
    # ======================================================

    def __altura_no(self, atual: No[T]|None) -> int:
        """
        Retorna a altura armazenada de um nó.

        TODO:
        - Retornar -1 se o nó for None.
        - Caso contrário, retornar sua altura armazenada.
        """
        if atual is None:
            return -1
        
        return atual.altura

    def __atualizar_altura(self, atual: No[T]) -> None:
        """
        Atualiza a altura de um nó a partir das alturas dos filhos.

        TODO:
        Aplicar a definição recursiva da altura.
        """
        atual_esquerda = self.__altura_no(atual.esquerda)
        atual_direita = self.__altura_no(atual.direita)
        atual.altura = 1 + max(atual_esquerda, atual_direita)

    def __fator_balanceamento(self, atual: No[T]) -> int:
        """
        Calcula o fator de balanceamento de um nó.

        Convenção:
            FB = altura(esquerda) - altura(direita)

        TODO:
        Calcular e retornar o fator de balanceamento.
        """
        return self.__altura_no(atual.esquerda) - self.__altura_no(atual.direita)

    # ======================================================
    # ROTAÇÕES
    # ======================================================

    def __rotacao_direita(self, atual: No[T]) -> No[T]:
        """
        Executa uma rotação simples à direita.

        Exemplo:

                   30                 20
                  / \\              /  \\
                20   A    ==>      10   30
               /  \\                   /  \\
             10     B                 B    A

        TODO:
        - Identificar o filho que assumirá a posição atual.
        - Reorganizar as referências dos nós.
        - Atualizar as alturas na ordem correta.
        - Retornar a nova raiz da subárvore.
        """
        nova_raiz = atual.esquerda
        filho_direita = atual
        filho_direita.esquerda = nova_raiz.direita
        nova_raiz.direita = filho_direita

        self.__atualizar_altura(filho_direita)
        self.__atualizar_altura(nova_raiz)

        return nova_raiz

    def __rotacao_esquerda(self, atual: No[T]) -> No[T]:
        """
        Executa uma rotação simples à esquerda.

        TODO:
        - Identificar o filho que assumirá a posição atual.
        - Reorganizar as referências dos nós.
        - Atualizar as alturas na ordem correta.
        - Retornar a nova raiz da subárvore.
        """
        nova_raiz = atual.direita
        filho_esquerda = atual
        filho_esquerda.direita = nova_raiz.esquerda
        nova_raiz.esquerda = filho_esquerda

        self.__atualizar_altura(filho_esquerda)
        self.__atualizar_altura(nova_raiz)

        return nova_raiz

    def __rebalancear(self, atual: No[T]) -> No[T]:
        """
        Atualiza a altura e rebalanceia uma subárvore.

        TODO:
        - Atualizar a altura do nó.
        - Calcular seu fator de balanceamento.
        - Identificar os casos LL, RR, LR e RL.
        - Executar a rotação simples ou dupla adequada.
        - Retornar a raiz atualizada da subárvore.
        """
        self.__atualizar_altura(atual)
        fb = self.__fator_balanceamento(atual)

        if fb > 1:
            if self.__fator_balanceamento(atual.esquerda) >= 0:
                atual = self.__rotacao_direita(atual)
            else:
                atual.esquerda = self.__rotacao_esquerda(atual.esquerda)
                atual = self.__rotacao_direita(atual)
        elif fb < -1:
            if self.__fator_balanceamento(atual.direita) <= 0:
                atual = self.__rotacao_esquerda(atual)
            else:
                atual.direita = self.__rotacao_direita(atual.direita)
                atual = self.__rotacao_esquerda(atual)

        return atual

    def remover(self, valor: T) -> None:
        """
        Remove `valor` da árvore, preservando a propriedade de AVL.

        Se `valor` não estiver presente na árvore, a árvore não é
        modificada.

        A remoção pode ocorrer em três situações:
            - o nó removido não possui filhos;
            - o nó removido possui apenas um filho;
            - o nó removido possui dois filhos. Nesse caso, o nó é
            suAVLituído pelo seu sucessor em ordem.

        Pré-requisito:
        `valor` deve ser comparável com os valores armazenados
        na árvore.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> for valor in [50, 30, 80, 20, 40, 70, 90]:
        ...     arvore.inserir(valor)

        >>> arvore.remover(20)
        >>> arvore.em_ordem()
        [30, 40, 50, 70, 80, 90]

        >>> arvore.remover(30)
        >>> arvore.em_ordem()
        [40, 50, 70, 80, 90]

        >>> arvore.remover(80)
        >>> arvore.em_ordem()
        [40, 50, 70, 90]

        >>> arvore.remover(100)
        >>> arvore.em_ordem()
        [40, 50, 70, 90]
        """
        self.__raiz = self.__remover(self.__raiz, valor)
        
    def __remover(self, atual: No[T]|None, valor: T) -> No[T] | None:
        """
        Remove recursivamente um valor e rebalanceia a subárvore.

        TODO:
        1. Tratar o caso em que o nó é None.
        2. Procurar o valor conforme a propriedade de AVL.
        3. Preservar os três casos de remoção da AVL.
        4. Reutilizar __sucessor no caso de dois filhos.
        5. Atualizar a altura dos nós restantes.
        6. Rebalancear ao retornar da recursão.
        7. Retornar a nova raiz da subárvore.
        """
        if atual is None:
           return None
        
        if atual.valor > valor:
           atual.esquerda = self.__remover(atual.esquerda, valor)
        elif atual.valor < valor:
           atual.direita = self.__remover(atual.direita, valor)
        else:
           if atual.esquerda is None and atual.direita is None:
               return None
           elif atual.esquerda is None:
               return atual.direita
           elif atual.direita is None:
               return atual.esquerda
           else:
               sucessor = self.__sucessor(atual)
               atual.valor = sucessor
               atual.direita = self.__remover(atual.direita, sucessor)

        return self.__rebalancear(atual)

    def __sucessor(self, atual: No[T]) -> T:
        sucessor = atual.direita
        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda
        return sucessor.valor