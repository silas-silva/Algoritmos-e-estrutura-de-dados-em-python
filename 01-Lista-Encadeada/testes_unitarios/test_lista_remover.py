from lista.ListaEncadeada import Lista
import pytest


def test_deletar_primeiro_elemento_com_funcao_deletar_primeiro_elemento():
    """
        Testar a remoção do primeiro elemento da lista, chamando o método deletar_primeiro()
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")

    dado : int = lista.deletar_primeiro()

    # Foi Removido o primeiro elemento que tem valor "Noé"
    assert dado == "Noé"


def test_deletar_primeiro_elemento_com_funcao_deletar_primeiro_elemento_com_lista_vazia():
    """
        Testar se remover elementos da lista estando vazia gera um indexError
    """
    lista : Lista = Lista()
    
    with pytest.raises(IndexError):
        lista.deletar_primeiro()
    

def test_deletar_primeiro_elemento_com_funcao_deletar_primeiro_elemento_diminui_quantidade():
    """
        Testar se quando remove elemento da lista, o tamanho da mesma também diminui
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")

    lista.deletar_primeiro()

    assert lista.quantidade == 2


def test_deletar_primeiro_elemento_com_funcao_deletar_primeiro_elemento_não_perde_as_referencias_posteriores():
    """
        Verificar se quando remove o primeiro elemento da lista
        Os dado posteriores são mantidos
    """
    lista : Lista = Lista()
    lista.adicionar(2) # indice 0
    lista.adicionar(3) # indice 1
    lista.adicionar(4) # indice 2
    lista.adicionar(7) # indice 3
    lista.adicionar(6) # indice 4

    dado : int = lista.deletar_primeiro()
    
    # O novo indice 0 deve ser o valor 3
    dado : int = lista.deletar_primeiro()

    assert dado == 3


def test_deletar_ultimo_elemento_com_funcao_deletar_ultimo_elemento():
    """
        Testar a remoção do último elemento da lista, chamando o método deletar_ultimo()
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    dado : int = lista.deletar_ultimo()

    # Foi Removido o último elemento que tem valor 4
    assert dado == 4


def test_deletar_ultimo_elemento_com_funcao_deletar_ultimo_elemento_com_lista_vazia():
    """
        Testar se remover elementos da lista estando vazia gera um indexError
    """
    lista : Lista = Lista()
    
    with pytest.raises(IndexError):
        lista.deletar_ultimo()


def test_deletar_ultimo_elemento_com_funcao_deletar_ultimo_elemento_diminui_quantidade():
    """
        Testar se quando remove elemento da lista, o tamanho da lista também diminui
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")

    lista.deletar_ultimo()

    assert lista.quantidade == 2


def test_deletar_elemento_da_lista_por_indice():
    """
        Testar a remoção de algum elemento da lista pelo indice
    """
    lista : Lista = Lista()
    lista.adicionar(2) # indice 0
    lista.adicionar(3) # indice 1
    lista.adicionar(4) # indice 2
    lista.adicionar(7) # indice 3
    lista.adicionar(6)

    dado : int = lista.deletar_por_indice(3)

    # Foi Removido o elemento na posição 1 que é o numero 7
    assert dado == 7


def test_deletar_elemento_da_lista_por_indice_diminui_quantidade():
    """
        Testar se quando remove elemento da lista, o tamanho da lista também diminui
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")

    lista.deletar_por_indice(1)

    assert lista.quantidade == 2


def test_deletar_elemento_da_lista_por_indice_não_perde_as_referencias_posteriores():
    """
        Verificar se quando remove algum elemento da lista pelo indice
        Os dado posteriores são mantidos
    """
    lista : Lista = Lista()
    lista.adicionar(2) # indice 0
    lista.adicionar(3) # indice 1
    lista.adicionar(4) # indice 2
    lista.adicionar(7) # indice 3
    lista.adicionar(6) # indice 4

    dado : int = lista.deletar_por_indice(3)
    
    # O novo indice 3 deve ser o valor 6
    dado : int = lista.deletar_por_indice(3)

    assert dado == 6


def test_deletar_primeiro_elemento_da_lista_por_indice():
    """
        Testar a remoção do primeiro elemento da lista pelo indice
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    dado : int = lista.deletar_por_indice(0)

    # Foi Removido o elemento na posição 0 que é o numero 2
    assert dado == 2


def test_deletar_ultimo_elemento_da_lista_por_indice():
    """
        Testar a remoção do último elemento da lista pelo indice
    """
    lista : Lista = Lista()
    lista.adicionar(2) # indice 0
    lista.adicionar(3) # indice 1
    lista.adicionar(4) # indice 2

    dado : int = lista.deletar_por_indice(2)

    # Foi Removido o elemento na posição 2 que é o numero 4
    assert dado == 4


def test_deletar_por_indice_passando_string():
    """
        Testar a remoção por posição passando uma string invés de um número e esperar um ValueError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(ValueError):
        lista.deletar_por_indice("2")


def test_deletar_por_indice_passando_indice_invalido_menor_que_0():
    """
         Testar a remoção por posição passando um índice invalido menor que 0 e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(IndexError):
        lista.deletar_por_indice(-1)


def test_deletar_por_indice_passando_indice_invalido_maior_que_a_lista():
    """
         Testar a remoção por posição passando um índice invalido maior que a lista e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(IndexError):
        lista.deletar_por_indice(3)

