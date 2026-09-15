from pilha import Pilha

def bem_formada(expressao: str) -> bool:
    """
    Verifica se os símbolos de agrupamento de uma expressão
    estão corretamente balanceados e aninhados.

    A expressão pode conter parênteses (), colchetes [] e
    chaves {}.

    Parâmetros:
        expressao: sequência de caracteres a ser verificada.

    Retorna:
        True se os símbolos estiverem corretamente formados;
        False caso contrário.

    Exemplos:
        >>> bem_formada("([]{})")
        True

        >>> bem_formada("([)]")
        False

        >>> bem_formada("{[()()]}")
        True

        >>> bem_formada("((())")
        False

        >>> bem_formada("}{")
        False
    """
    pilha = Pilha(len(expressao))
    for i in expressao:
        if i == "(" or i == "[" or i == "{":
            pilha.push(i)
        elif i == ")" or i == "]" or i == "}":
            if pilha.is_empty():
                return False
            if pilha.top() == "(" and i != ")" or pilha.top() == "[" and i != "]" or pilha.top() == "{" and i != "}":
                return False
            pilha.pop()
    return pilha.is_empty()