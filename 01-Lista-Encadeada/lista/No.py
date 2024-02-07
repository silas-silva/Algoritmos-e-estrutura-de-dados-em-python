class No(object):

    def __init__(self, dado : object) -> None:
        """
            Construtor da classe Nó

            Args:
                dado (object): dado a ser colocado no nó
        """
        self.dado: object = dado
        self.proximo: No = None