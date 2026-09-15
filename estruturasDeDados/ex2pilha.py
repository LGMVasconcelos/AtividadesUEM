from pilha import Pilha

class Editor:
    """
    Representa um editor de texto simplificado que mantém
    um histórico de operações, permitindo desfazer e refazer.

    O histórico deve ser implementado utilizando TADs Pilha.

    Uma operação realizada é adicionada ao histórico de
    operações que podem ser desfeitas.

    Quando uma operação é desfeita, ela passa a fazer parte
    do histórico de operações que podem ser refeitas.

    Quando uma nova operação é realizada após um desfazer(),
    todas as operações que poderiam ser refeitas são
    descartadas.

    Exemplos:
        >>> editor = Editor()
        >>> editor.realizar("A")
        >>> editor.realizar("B")
        >>> editor.realizar("C")
        >>> editor.estado()
        ['A', 'B', 'C']

        >>> editor.desfazer()
        'C'
        >>> editor.estado()
        ['A', 'B']

        >>> editor.refazer()
        'C'
        >>> editor.estado()
        ['A', 'B', 'C']

        >>> editor.desfazer()
        'C'
        >>> editor.realizar("D")
        >>> editor.estado()
        ['A', 'B', 'D']

        >>> editor.pode_refazer()
        False
    """

    def __init__(self):
        """
        Cria um editor inicialmente sem operações realizadas.
        """
        self.__historico = Pilha[object](1000)
        self.__refazendo = Pilha[object](1000)

    def realizar(self, operacao):
        """
        Realiza uma nova operação.

        A operação deve ser adicionada ao histórico de operações
        que podem ser desfeitas.

        Uma nova operação realizada depois de um desfazer()
        elimina todas as operações que poderiam ser refeitas.

        Parâmetros:
            operacao: operação a ser realizada.
        """
        while not self.__refazendo.is_empty():
            self.__refazendo.pop()

        self.__historico.push(operacao)

    def desfazer(self):
        """
        Desfaz a última operação realizada.

        Retorna:
            A operação que foi desfeita.

        Levanta:
            IndexError se não houver operação para desfazer.
        """
        if self.__historico.is_empty():
            raise IndexError('não há operação para desfazer')

        operacao = self.__historico.pop()
        self.__refazendo.push(operacao)
        return operacao

    def refazer(self):
        """
        Refaz a última operação que havia sido desfeita.

        Retorna:
            A operação que foi refeita.

        Levanta:
            IndexError se não houver operação para refazer.
        """
        if self.__refazendo.is_empty():
            raise IndexError('não há operação para refazer')

        operacao = self.__refazendo.pop()
        self.__historico.push(operacao)
        return operacao

    def estado(self):
        """
        Retorna a sequência de operações atualmente realizadas.

        Retorna:
            Uma lista contendo as operações realizadas na ordem
            em que estão atualmente aplicadas.
        """
        pilha_aux = Pilha[object](1000)
        resultado = []

        while not self.__historico.is_empty():
            operacao = self.__historico.pop()
            resultado.append(operacao)
            pilha_aux.push(operacao)

        while not pilha_aux.is_empty():
            self.__historico.push(pilha_aux.pop())

        return list(reversed(resultado))

    def pode_desfazer(self):
        """
        Informa se existe alguma operação que pode ser desfeita.

        Retorna:
            True se houver uma operação para desfazer;
            False caso contrário.
        """
        return not self.__historico.is_empty()

    def pode_refazer(self):
        """
        Informa se existe alguma operação que pode ser refeita.

        Retorna:
            True se houver uma operação para refazer;
            False caso contrário.
        """
        return not self.__refazendo.is_empty()