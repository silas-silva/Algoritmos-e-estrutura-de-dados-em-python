from app.ListaDuplamenteEncadeada import Lista
from app.Inteiro import Inteiro
import pytest

def test_adicionarObjetoNaLista():
    """
        Testar a adição de elementos na lista
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))

    # Foi adicionado 1 elemento
    assert lista.quantidade == 1


def test_deletar_primeiro_elemento_com_funcao_deletar_primeiro_elemento():
    """
        Testar a remoção do primeiro elemento da lista, chamando o método deletar_primeiro()
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    dado : Inteiro = lista.deletar_primeiro()

    # Foi Removido o primeiro elemento que tem valor 2
    assert dado.num == 2


def test_deletar_ultimo_elementoCom_funcao_deletar_ultimo_elemento():
    """
        Testar a remoção do último elemento da lista, chamando o método deletar_ultimo()
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    dado : Inteiro = lista.deletar_ultimo()

    # Foi Removido o último elemento que tem valor 4
    assert dado.num == 4


def test_deletar_elementoD_da_lista_por_posição():
    """
        Testar a remoção de algum elemento da lista pela posição
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))
    lista.adicionar(Inteiro(7))
    lista.adicionar(Inteiro(6))

    dado : Inteiro = lista.deletar_indice(3)

    # Foi Removido o elemento na posição 1 que é o numero 7
    assert dado.num == 7


def test_deletar_primeiro_elemento_da_lista_por_indice():
    """
        Testar a remoção do primeiro elemento da lista pela posição
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    dado : Inteiro = lista.deletar_indice(0)

    # Foi Removido o elemento na posição 0 que é o numero 2
    assert dado.num == 2


def test_deletar_ultimo_elemento_da_lista_por_indice():
    """
        Testar a remoção do último elemento da lista pela posição
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    dado : Inteiro = lista.deletar_indice(2)

    # Foi Removido o elemento na posição 2 que é o numero 4
    assert dado.num == 4


def test_deletar_por_indice_passando_string():
    """
        Testar a remoção por posição passando uma string invés de um número e esperar um ValueError
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    with pytest.raises(ValueError):
        lista.deletar_indice("2")



def test_deletar_por_indice_passando_indice_invalido_menor_que_0():
    """
         Testar a remoção por posição passando um índice invalido menor que 0 e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    with pytest.raises(IndexError):
        lista.deletar_indice(-1)


def test_deletar_por_indice_passando_indice_invalido_maior_que_a_lista():
    """
         Testar a remoção por posição passando um índice invalido maior que a lista e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))

    with pytest.raises(IndexError):
        lista.deletar_indice(3)




def test_verificar_tamanho_da_lista_sem_remover_objetos():
    """
        Testar a quantidade de elementos da lista corresponde a quantos elementos foram inseridos
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(2))

    assert lista.quantidade == 5
    

def test_verificar_tamanho_da_lista_depois_de_remover_ultimo_objeto():
    """
        Testar a quantidade de elementos da lista é mudado quando remove objetos pela função de remover ultimo objeto
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(2))
    lista.deletar_ultimo()

    assert lista.quantidade == 4


def test_verificar_tamanho_da_lista_depois_de_remover_primeiro_objeto():
    """
        Testar a quantidade de elementos da lista é mudado quando remove objetos pela função de remover primeiro objeto
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(2))
    lista.deletar_primeiro()

    assert lista.quantidade == 4


def test_verificar_tamanho_da_lista_depois_de_remover_objeto_por_indice():
    """
        Testar a quantidade de elementos da lista é mudado quando remove objetos pelo indice
    """
    lista : Lista = Lista()
    lista.adicionar(Inteiro(2))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(4))
    lista.adicionar(Inteiro(3))
    lista.adicionar(Inteiro(2))
    lista.deletar_indice(2)

    assert lista.quantidade == 4