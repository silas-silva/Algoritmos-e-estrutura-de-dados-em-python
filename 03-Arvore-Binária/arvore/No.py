class No(object):
    
    def __init__(self, dado : object) -> None:
        """
            Construtor da classe Nó

            Args:
                objeto (object): Objeto a ser colocado no nó
        """
        self.dado : object = dado
        self.direita : No = None
        self.esquerda : No = None