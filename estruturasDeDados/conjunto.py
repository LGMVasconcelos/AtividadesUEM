from __future__ import annotations

from typing import Generic, TypeVar


from avl import AVL


T = TypeVar("T")


class Conjunto(Generic[T]):
    """Conjunto implementado sobre uma Árvore AVL (sem duplicatas)."""

    def __init__(self, elementos_iniciais: list[T] | None = None) -> None:
        self.__arvore: AVL[T] = AVL()
        if elementos_iniciais is not None:
            for elemento in elementos_iniciais:
                self.adicionar(elemento)

    def elementos(self) -> list[T]:
        """Retorna os elementos em ordem crescente."""
        return self.__arvore.em_ordem()

    def adicionar(self, x: T) -> None:
        """Adiciona x ao conjunto."""
        self.__arvore.inserir(x)

    def pertence(self, x: T) -> bool:
        """Retorna True se x pertence ao conjunto."""
        return self.__arvore.buscar(x)

    def remover(self, x: T) -> None:
        """Remove x do conjunto, se existir."""
        self.__arvore.remover(x)

    def vazio(self) -> bool:
        """Retorna True se o conjunto estiver vazio."""
        return self.__arvore.esta_vazia()

    def cardinalidade(self) -> int:
        """Retorna a quantidade de elementos do conjunto."""
        return self.__arvore.quantidade()

    def uniao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """Retorna um novo conjunto com os elementos de self e outro."""
        resultado = Conjunto[T](self.elementos())
        for elemento in outro.elementos():
            if not resultado.pertence(elemento):
                resultado.adicionar(elemento)
        return resultado

    def intersecao(self, outro: Conjunto[T]) -> Conjunto[T]:
        """Retorna um novo conjunto com os elementos comuns."""
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if outro.pertence(elemento):
                resultado.adicionar(elemento)

        return resultado

    def contido(self, outro: Conjunto[T]) -> bool:
        """Retorna True se self é subconjunto de outro."""
        if self.cardinalidade() > outro.cardinalidade():
            return False

        for elemento in self.elementos():
            if not outro.pertence(elemento):
                return False

        return True

    def diferenca(self, outro: Conjunto[T]) -> Conjunto[T]:
        """Retorna um novo conjunto com os elementos de self que não estão em outro."""
        resultado = Conjunto[T]()
        for elemento in self.elementos():
            if not outro.pertence(elemento):
                resultado.adicionar(elemento)
        return resultado
