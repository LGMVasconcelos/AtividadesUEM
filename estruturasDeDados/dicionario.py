from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


@dataclass
class No(Generic[K, V]):
    """
    Representa um nó de uma árvore binária de busca.

    Cada nó armazena um valor, uma altura e possui referências para,
    no máximo, dois filhos: esquerdo e direito.
    """

    chave: K
    valor: V
    altura: int = 0
    esquerda: No[K, V] | None = None
    direita: No[K, V] | None = None



class Dict(Generic[K, V]):
    """
    Tipo AAVLrato de Dados Árvore AVL 
    (Georgy Adelson-Velsky e Yevgeniy Landis).

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

    def inserir(self, chave: K, valor: V) -> None:
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
        self.__raiz = self.__inserir(self.__raiz, chave, valor)
        
    def __inserir(self, atual: No[K, V]|None, chave: K, valor: V) -> No[K, V]:
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
           return No(chave, valor)
        
        if atual.valor > valor:
           atual.esquerda = self.__inserir(atual.esquerda, valor)
        elif atual.valor < valor:
           atual.direita = self.__inserir(atual.direita, valor)

        self.__atualizar_altura(atual)
        self.__rebalancear(atual)

        return atual

    def alterar(self, chave: K, valor: V) -> None:
        """
        Altera o valor associado a `chave` no dicionário.

        Pré-requisito:
        `valor` deve ser comparável com os valores armazenados
        na árvore.

        Se `chave` não estiver presente, a árvore não é modificada.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.inserir(50)
        >>> arvore.inserir(30)
        >>> arvore.inserir(80)

        >>> arvore.alterar(30, 35)
        >>> arvore.em_ordem()
        [35, 50, 80]

        >>> arvore.alterar(70, 75)
        >>> arvore.em_ordem()
        [35, 50, 80]
        """
        if self.contem(chave):
            self.__raiz = self.__alterar(self.__raiz, chave, valor)

    def __alterar(self, atual: No[K, V], chave: K, valor: V) -> No[K, V]:
        
        if atual.chave > chave:
            atual.esquerda = self.__alterar(atual.esquerda, chave, valor)
        elif atual.chave < chave:
            atual.direita = self.__alterar(atual.direita, chave, valor)
        else:
            atual.valor = valor

        return atual

    def contem(self, chave: K) -> bool:
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

        >>> arvore.contem(30)
        True

        >>> arvore.contem(70)
        False
        """
        return self.buscar(chave)

    def buscar(self, chave: K) -> bool:
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
        return self.__buscar(self.__raiz, chave)
    
    def __buscar(self, atual: No[K, V]|None, chave: K) -> bool:
        if atual is None:
            return False
        
        if atual.chave > chave:
            return self.__buscar(atual.esquerda, chave)
        
        if atual.chave < chave:
            return self.__buscar(atual.direita, chave)
        
        return True



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
    
    def __em_ordem(self, atual: No[K, V]|None) -> list[V]:
        if atual is None:
            return []
        return self.__em_ordem(atual.esquerda) + [atual.valor] + self.__em_ordem(atual.direita)



    def tamanho(self) -> int:
        """
        Retorna o tamanho do dicionário.

        Exemplos
        --------
        >>> arvore = AVL[int]()
        >>> arvore.tamanho()
        0

        >>> for valor in [50, 30, 80]:
        ...     arvore.inserir(valor)

        >>> arvore.tamanho()
        3
        """
        return self.__tamanho(self.__raiz)
        

    def __tamanho(self, atual: No[K, V]|None) -> int:
        if atual is None:
            return 0
        return 1 + self.__tamanho(atual.esquerda) + self.__tamanho(atual.direita)


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

    def __altura_no(self, atual: No[K, V]) -> int:
        """
        Retorna a altura armazenada de um nó.

        TODO:
        - Retornar -1 se o nó for None.
        - Caso contrário, retornar sua altura armazenada.
        """
        if atual is None:
            return -1
        
        return atual.altura

    def __atualizar_altura(self, atual: No[K, V]) -> None:
        """
        Atualiza a altura de um nó a partir das alturas dos filhos.

        TODO:
        Aplicar a definição recursiva da altura.
        """
        atual_esquerda = self.__altura_no(atual.esquerda)
        atual_direita = self.__altura_no(atual.direita)
        atual.altura = 1 + max(atual_esquerda, atual_direita)

    def __fator_balanceamento(self, atual: No[K, V]|None) -> int:
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

    def __rotacao_direita(self, atual: No[K, V]) -> No[K, V]:
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

    def __rotacao_esquerda(self, atual: No[K, V]) -> No[K, V]:
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
        nova_raiz.direita = filho_esquerda

        self.__atualizar_altura(filho_esquerda)
        self.__atualizar_altura(nova_raiz)

        return nova_raiz

    def __rebalancear(self, atual: No[K, V]) -> No[K, V]:
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
            if self.__fator_balanceamento(atual.direita) >= 0:
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
        
    def __remover(self, atual: No[K, V]|None, valor: K) -> No[K, V] | None:
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

        self.__atualizar_altura(atual)
        self.__rebalancear(atual)

        return atual

    def __sucessor(self, atual: No[K, V]) -> V:
        sucessor = atual.direita
        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda
        return sucessor.valor