### Pre Requisitos:
- POO (Programação orientada a Objetos)
- Python


### Lista encadeada
Uma lista encadeada é uma estrutura de dados linear e dinamica que guarda n dados quaisquer (o dado pode ser um valor primitivo ou um objeto), também guarda a posição para o próximo elemento da lista, ou seja, em uma posição de memória é guardado o dado atual e também guardado o endereço de memória que o próximo dado está guardado (é guardado o dado e um ponteiro para o próximo dado) e sempre o último dado da lista não aponta para nada, ou seja o ponteiro dele é "null"

Exemplo: Imagine uma fila de pessoas, onde a primeira sabe onde a segunda pessoa está, mas não sabe onde as demais pessoas estão, mas a segunda sabe onde está a terceira, e por sua vez a terceira sabe onde está a quarta, até chegar na ultima pessoa da fila. Cada pessoa tem um nome (o dado armazenado) e tem a informação de onde está a próxima pessoa (o ponteiro), abaixo veja minhas incriveis habilidades  de desenho kkkk.

![Fila de Pessoas](readme_imagens/fila%20%20pessoas.png)

Para entender listas, primeiro é necessario definir o conceito de "nó", o "nó" seria uma pessoa dessa fila, ou seja o "nó" é um objeto que tem um objeto pessoa e tem um link (ou um ponteiro) para o próximo objeto do tipo "nó", podemos definir esse "nó" como uma classe que tem o dado ou objeto que queremos e também tem outro atributo do tipo "nó".

- Exemplo em python do "nó"

    ```python

    def __init__(self, objeto : object) -> None:
        """
            Construtor da classe Nó
            Args:
                objeto (object): Objeto a ser colocado no nó
        """
        self.objeto: object = objeto
        self.proximo: No = None

    ```

- Exemplo em python do "nó" para Pessoa

    ```python

    def __init__(self, pessoaFila : Pessoa) -> None:
        """
            Construtor da classe Nó
            Args:
                objeto (Pessoa): Objeto Pessoa a ser colocado no Nó
        """
        self.pessoa: Pessoa = pessoaParam
        self.proximo: No = None

    ```
    Uma pessoa na fila que sabe a localização da próxima pessoa da fila.

- ###### Exemplo Visual comumente usado para representar lista encadeada
![Lista encadeada](readme_imagens/lista_encadeada.png)


#### Implementações
* Lista encadeada: Na pasta `app`
* Testes na pasta `testUnitarios`


### Rodar os testes
- Clonar/baixar essa pasta (Essa é pasta raiz da Lista encadeada)
- para rodar todos os testes unitários:
    Na raiz do projeto executar no bash/cmd o comando
    ```bash
      pytest testUnitarios
    ```
    
- Para gerar um relatório de cobertura de código em HTML:
    Na raiz do projeto executar no bash/cmd o comando
    ```bash
      pytest
    ```