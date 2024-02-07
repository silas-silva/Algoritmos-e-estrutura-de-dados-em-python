class No(object):

    def __init__(self, dado : object) -> None:
        """
            Construtor da classe Nó

            Args:
                dado (object): Objeto a ser colocado no nó
        """
        self.dado: object = dado
        self.anterior: No = None
        self.proximo: No = None