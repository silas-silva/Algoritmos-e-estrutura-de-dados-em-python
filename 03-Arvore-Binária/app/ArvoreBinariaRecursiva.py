from app.No import No

class ArvoreBinariaRecursiva(object):
    
    def __init__(self) -> None:
        """
            Construtor da Arvore Binária recursiva

            Args:
                objeto (object): Objeto a ser colocado como o dado da arvore, o objeto deve ter um atributo do tipo dado para ser o identificador de ordem
        
        """
        self.raiz = None
        self.tamanho = 0
    
    
    def adicionar(self, objeto : object, raiz : No = None) -> None:
        """
           Adiciona um elemento na árvoria binária

           Args:
               objeto (object): objeto a ser inserido na lista, o objeto preciso ter um atributo com nome "dado" do tipo inteiro
        """
        if self.raiz == None:
            self.raiz = No(objeto)
            self.tamanho += 1
            return
        self.auxiliar_no_adicionar(objeto, self.raiz)
    
    
    def auxiliar_no_adicionar(self, objeto : object, raiz : No) -> None:
        """
           Método interno/privado que só a classe tem acesso, usado para auxiliar no método adicionar
        """
        if(objeto.dado > raiz.objeto.dado):
            # maior, insere na direita
            if raiz.direita == None: # Se direita não tiver dado, insere logo, se tiver, verificar o proximo nó
                raiz.direita = No(objeto)
                self.tamanho += 1
            else:
                self.auxiliar_no_adicionar(objeto, raiz.direita)
        
        elif(objeto.dado < raiz.objeto.dado):
            #menor, insere na esquerda
            if raiz.esquerda == None: # Se esquerda não tiver dado, insere logo, se tiver, verificar o proximo nó
                raiz.esquerda = No(objeto)
                self.tamanho += 1
            else:
                self.auxiliar_no_adicionar(objeto, raiz.esquerda)

    
    def deletar_por_numero(self, numero) -> object:
        """
           Deleta um elemento da lista baseado no número do atributo "dado" do objeto

           Args:
               numero (int): número que está no objeto a ser deletado

           Returns:
               objeto (object) : objeto deletado da arvore
        """
        pass
    
    
    # def imprimir(self) -> None:
    #     print("Lado direito:")
    #     aux : No = self.raiz
    #     while aux != None:
    #         print(aux.objeto.dado)
    #         aux = aux.direita
        
    #     print("Lado Esquerdo:")
    #     aux : No = self.raiz
    #     while aux != None:
    #         print(aux.objeto.dado)
    #         aux = aux.esquerda

