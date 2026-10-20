from arranjo import Arranjo

def busca_sequencial(a: Arranjo, valor: int) -> int:
    for i in range(a.__len__()):
        if a.__getitem__(i) == valor:
            return i
    return -1

def busca_binaria(a: Arranjo, valor: int, esq: int, dir: int) -> int:
    if esq > dir:
        return -1
    meio = (esq + dir) // 2
    if a.__getitem__(meio) == valor:
        return meio
    if a.__getitem__(meio) < valor:
        return busca_binaria(a, valor, meio + 1, dir)
    return busca_binaria(a, valor, esq, meio - 1)