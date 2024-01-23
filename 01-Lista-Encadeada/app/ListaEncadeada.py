from app.No import No

class Lista(object):

    def __init__(self) -> None:
        """
            Construtor da classe Lista
        """
        self.raiz: No = None
        self.quantidade: int = 0


    def adicionar(self, objeto : object) -> None:
        """
           Adiciona um objeto na ultima posição da lista

           Args:
               objeto (object): Objeto a ser colocado na lista.
        """
        if self.raiz == None:
            self.raiz = No(objeto)
            self.quantidade += 1
        else:
            aux: No = None
            aux = self.raiz
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = No(objeto)
            self.quantidade += 1


    def deletar_ultimo(self) -> object:
        """
           Deleta o ultimo elemento da lista

           Returns:
               objeto_retornar (object) : Valor deletado da lista
       """
        aux: No = None
        aux_proximo: No = None
        aux = self.raiz
        aux_proximo = self.raiz.proximo

        while aux_proximo.proximo != None:
            aux = aux.proximo
            aux_proximo = aux_proximo.proximo
        objeto_retornar: int = aux.proximo.objeto
        aux.proximo = None
        self.quantidade -= 1
        return objeto_retornar


    def deletar_primeiro(self) -> object:
        """
           Deleta o primeiro elemento da lista

           Returns:
               dado_retornar (object) : Valor deletado da lista
       """
        objeto_retornar: int = self.raiz.objeto
        self.raiz = self.raiz.proximo
        self.quantidade -= 1
        return objeto_retornar


    def deletar_indice(self, indice) -> object:
        """
           Deleta um elemento da lista baseado na posição

           Args:
               indice (int): posição do elemento a ser deletado.

           Returns:
               dado_retornar (object) : Valor deletado da lista
        """
        
        # Verificação de errors
        if not isinstance(indice, int):
            raise ValueError("A função espera um número inteiro")
        
        if indice < 0 or indice >= self.quantidade:
            raise IndexError(f"O índice {indice} está fora dos limites da lista.")

        if indice == 0:
            return self.deletar_primeiro()
        elif indice == (self.quantidade - 1):
            return self.deletar_ultimo()
        else:
            aux: No = None
            aux = self.raiz
            cont = 1
            while aux.proximo != None:
                if cont == indice:
                    # Deletar
                    dado_retornar: int = aux.proximo.objeto
                    aux.proximo = aux.proximo.proximo
                    self.quantidade -= 1
                    return dado_retornar
                cont += 1
                aux = aux.proximo

