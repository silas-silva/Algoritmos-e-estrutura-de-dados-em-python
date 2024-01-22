class No(object):

    def __init__(self, objeto : object) -> None:
        """
            Construtor da classe Nó

            Args:
                objeto (object): Objeto a ser colocado no nó
        """
        self.objeto: object = objeto
        self.proximo: No = None