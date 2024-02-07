from lista.No import No

class Lista(object):

    def __init__(self) -> None:
        """
            Construtor da classe Lista
        """
        self.raiz: No = None
        self.quantidade: int = 0


    def adicionar(self, dado : object) -> None:
        """
           Adiciona um objeto na ultima posição da lista

           Args:
               dado (object): dado a ser colocado na lista.
        """
        if self.raiz == None:
            self.raiz = No(dado)
            self.quantidade += 1
        else:
            auxiliar: No = None
            auxiliar = self.raiz
            while auxiliar.proximo != None:
                auxiliar = auxiliar.proximo
            auxiliar.proximo = No(dado)
            self.quantidade += 1


    def adicionar_inicio(self, dado : object) -> None:
        """
           Adiciona um objeto na primeira posição da lista

           Args:
               dado (object): dado a ser colocado na lista.
        """
        if self.raiz == None:
            self.raiz = No(dado)
            self.quantidade += 1
        else:
            auxiliar: No = self.raiz
            self.raiz = No(dado)
            self.raiz.proximo = auxiliar
            self.quantidade += 1


    def adicionar_por_indice(self, indice : int, dado : object):
        """
           Adiciona um objeto no indice especificado, o objeto que estava nesse indice anteriormente, será empurrado para a proxima posição

           Args:
               dado (object): dado a ser colocado na lista.
        """
        # Verificação de errors
        if not isinstance(indice, int):
            raise ValueError("A função espera um número inteiro")
        
        if indice < 0 or (indice >= self.quantidade and self.quantidade > 0):
            raise IndexError(f"O índice {indice} está fora dos limites da lista.")
        
        if self.raiz == None:
            self.raiz = No(dado)
            self.quantidade += 1
        else:
            if indice == 0:
                self.adicionar_inicio(dado)
            elif indice == (self.quantidade - 1):
                self.adicionar(dado)
            else:
                contador = 1
                auxiliar: No = self.raiz
                while auxiliar.proximo != None:
                    if indice == contador:
                        outro_auxiliar : No = auxiliar
                        auxiliar.proximo = No(dado)
                        auxiliar.proximo.proximo = outro_auxiliar
                        self.quantidade += 1
                        break
                    contador += 1
                    auxiliar = auxiliar.proximo


    def deletar_ultimo(self) -> object:
        """
           Deleta o ultimo elemento da lista

           Returns:
               objeto (object) : Valor deletado da lista
        """
        if self.raiz == None:
            raise IndexError(f"O índice 0 está fora dos limites da lista.")
        auxiliar: No = None
        auxiliar_proximo: No = None
        auxiliar = self.raiz
        auxiliar_proximo = self.raiz.proximo

        while auxiliar_proximo.proximo != None:
            auxiliar = auxiliar.proximo
            auxiliar_proximo = auxiliar_proximo.proximo
        objeto_retornar: int = auxiliar.proximo.dado
        auxiliar.proximo = None
        self.quantidade -= 1
        return objeto_retornar


    def deletar_primeiro(self) -> object:
        """
           Deleta o primeiro elemento da lista

           Returns:
               objeto (object) : Valor deletado da lista
        """
        if self.raiz == None:
            raise IndexError(f"O índice 0 está fora dos limites da lista.")
        
        objeto_retornar: int = self.raiz.dado
        self.raiz = self.raiz.proximo
        self.quantidade -= 1
        return objeto_retornar


    def deletar_por_indice(self, indice) -> object:
        """
           Deleta um elemento da lista baseado na posição

           Args:
               indice (int): posição do elemento a ser deletado.

           Returns:
               objeto (object) : Valor deletado da lista
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
            auxiliar: No = None
            auxiliar = self.raiz
            contador = 1
            while auxiliar.proximo != None:
                if contador == indice:
                    # Deletar
                    dado_retornar: object = auxiliar.proximo.dado
                    auxiliar.proximo = auxiliar.proximo.proximo
                    self.quantidade -= 1
                    return dado_retornar
                contador += 1
                auxiliar = auxiliar.proximo


    def buscar(self, dado : object) -> int:
        """
           Procura por um valor específico na lista encadeada. e retorna o indice do primeiro elemento encontrado.
           A função __eq__(self) deve ser definida na classe com o que fará os objetos serem iguais, o seu padrão de comparação

           Args:
               dado (int): objeto a ser comparado, e verificado se está na lista

           Returns:
               indice : Indice que o dado está localizado
        """
        auxiliar : No = self.raiz
        contador = 0
        while auxiliar != None:
            if auxiliar.dado == dado:
                return contador
            auxiliar = auxiliar.proximo
            contador += 1
        return -1 


    def busca_por_indice(self, indice : int) -> object:
        """
           Procura por um valor na lista encadeada dado seu indice

           Args:
               indice (int): posição do elemento a ser buscado.

           Returns:
               objeto (object) : Valor deletado da lista
        """
        # Verificação de errors
        if not isinstance(indice, int):
            raise ValueError("A função espera um número inteiro")
        
        if indice < 0 or indice >= self.quantidade:
            raise IndexError(f"O índice {indice} está fora dos limites da lista.")
        
        auxiliar : No = self.raiz
        contador = 0
        while auxiliar != None:
            if contador == indice:
                return auxiliar.dado
            auxiliar = auxiliar.proximo
            contador += 1


    def obter_tamanho(self) -> int:
        """
           Retorna a quantidade de elementos da lista, em outras palavras, o seu tamanho

           Returns:
               tamanho (int) : tamanho da lista
        """
        return self.quantidade


    def verificar_se_vazia(self) -> bool:
        """
           Retornar Verdadeiro se a lista tiver vazia, e Falso se não estiver

           Returns:
               estado (bool) : Estado da lista, vazio ou não
        """
        return True if self.raiz == None else False


    def atualizar_elemento_por_indice(self, indice : int, novo_dado : object) -> bool:
        """
            Atualiza o elemento em um indice especifico

            Args:
               indice (int): posição do elemento a ser atualizado.
               novo_dado (object): Novo dado a ser inserido
            
            Returns:
               sucesso (bool) : foi atualizado ou não True ou False
        """
        # Verificação de errors
        if not isinstance(indice, int):
            raise ValueError("A função espera um número inteiro")
        
        if indice < 0 or indice >= self.quantidade:
            raise IndexError(f"O índice {indice} está fora dos limites da lista.")
        auxiliar : No = self.raiz
        contador = 0
        while auxiliar != None:
            if contador == indice:
                auxiliar.dado = novo_dado
                return True
            contador += 1
            auxiliar = auxiliar.proximo
        return False


    def imprimir(self) -> bool:
        """
            Imprime os dados da lista, o objeto da lista deve ter a função __str__ retornando algo dado que pode ser impresso
           
            Returns:
               sucesso (bool) : se imprimiu os dados ou não
        """
        auxiliar : No = self.raiz
        while auxiliar != None:
            try:
                print(auxiliar.dado)
            except:
               return False 
            auxiliar = auxiliar.proximo
        return True
