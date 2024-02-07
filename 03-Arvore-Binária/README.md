nó 
Raiz
Folhas 
SubArvore
Floresta


Relações entre os nós
Nó pai
Nó Filho
Nó Descendente   ex: a -> b -> c   "c" é descendente de "a"
Nó Ancestral     ex: a -> b -> c   "a" é ancestral de "c"


Folha é um nó que não tem filhos


Arvore binaria tem que ter dois filhos, nem que esses filhos sejam vazios


Percurso em arvore : Traversal (Inglês)
""" 
    Existem diferentes formas de percorrer os nós de uma árvore binária:
    Inorder Traversal:
        Visita o nó esquerdo, depois o nó raiz e, por fim, o nó direito.
    Preorder Traversal:
        Visita o nó raiz, depois o nó esquerdo e, por fim, o nó direito.
    Postorder Traversal:
        Visita o nó esquerdo, depois o nó direito e, por fim, o nó raiz.
"""




# Conceitos importantes

## Caminho
Uma sequencia de nós que estão interligados

### Cumprimento de um caminho
Podem ser medidos em arestas ou em nós
É o numero total de nós ou arestas entre o nó inicial e o nó final

## Pronfundida
É o comprimento do caminho do nó (de maior profundidade) até a raiz (Exemplo, a raiz tem profundidade 1, os filhos da raiz, tem profundidade 2)
É o comprimento do caminho da raiz à folha de maior profundidade

Como encontrar a profundidade de uma arvore?
    Percorrer a arvore em Postorder Traversal (Pós ordem)

code

def altura(self, no : No = None):
    if no is None:
        no = self.raiz
    alturaEsquerda = 0
    alturaDireita = 0

    if no.esquerda:
        alturaEsquerda = self.altura(no.esquerda)
    if no.direita:
        alturaDireita = self.altura(no.direita)
    
    if alturaDireita > alturaEsquerda:
        return alturaDireita + 1
    else:
        return alturaEsquerda + 1


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None

def profundidade_arvore(raiz):
    if raiz is None:
        return 0
    else:
        profundidade_esquerda = profundidade_arvore(raiz.esquerdo)
        profundidade_direita = profundidade_arvore(raiz.direito)
        return max(profundidade_esquerda, profundidade_direita) + 1

# Exemplo de uso:
# raiz = No(1)
# raiz.esquerdo = No(2)
# raiz.direito = No(3)
# raiz.esquerdo.esquerdo = No(4)
# raiz.esquerdo.direito = No(5)
# print(profundidade_arvore(raiz))


                      a
                   /     \
                  b        f
                 / \        \
                c   d         g
               / \           / \ 
              e   l         h   s
               \ 
                 j

raiz = No(1)
raiz.esquerdo = No(2)
raiz.direito = No(3)
raiz.esquerdo.esquerdo = No(4)
raiz.esquerdo.direito = No(5)
raiz.esquerdo.esquerdo.esquerdo = No(6)




## Altura
É o comprimento de um nó, até seu descendente mais profundo, funciona de forma analoga à profundidade, imagine que agora esse nó que quero saber a altura é o nó raiz, logo, com ele sendo a raiz, sua profundidade, é a sua altura. EX: a -> b -> c -> d   : A altura de "a" é 4, A altura de "c" é 2, a altura de "d" é 1

### Altura maxima da arvore
Cairia no caso de colocar todos os dados em um lado da lista onde nenhum nó teria dois filhos preenchidos, a arvore ficaria parecendo uma lista encadeada, a altura maxima é dado por "max(x) sendo a função de altura maxima" max(x) = n

### Altura minima da arvore
Só desceria para o proximo nivel da arvore, caso todos os nós daquele nivel (daquela profundidade) já estivesse preenchidos, a altura minima é dada por "min(x) sendo a função de altura minima" min(x) = 1 + piso(log(n))


# Maior e menor elemento (Maximo e Minimo)

## Menor
É o elemento que está mais a esquerda é não tem filhos à esquerda
Pega o da esquerda da raiz, depois o da esquerda desse filho, e vai pegando o da esquerda, até não ter filhos

## Maior
É o elemento que está mais a direita é não tem filhos à direita
Pega o da direita da raiz, depois o da direita desse filho, e vai pegando o da direita, até não ter filhos


## Antecessor e Sucessor

### Sucessor
    É o menor elemento entre os maiores filhos de uma nó, ou seja, é o menor elemento do lado direito de um nó
    O sucessor de um nó em uma árvore binária é o nó que tem o menor valor maior que o valor do nó em questão. 

### Antecessor
    O antecessor de um nó é o nó que tem o maior valor menor que o valor do nó em questão.