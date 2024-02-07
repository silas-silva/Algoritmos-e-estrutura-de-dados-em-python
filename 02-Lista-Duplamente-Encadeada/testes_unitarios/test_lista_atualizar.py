from lista.ListaDuplamenteEncadeada import Lista
import pytest


def test_atualizar_dados_por_indice():
    """
        Testar a atualização do dado em um indice especifico
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")
    
    lista.atualizar_elemento_por_indice(1, "Sem")
    
    elemento = lista.busca_por_indice(1)
    
    assert elemento == "Sem"


def test_atualizar_dados_por_indice_passando_indice_maior_que_a_lista():
    """
        Testar acessar index não existente da lista e atualizar dado nesse index
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")
    
    with pytest.raises(IndexError):
        lista.atualizar_elemento_por_indice(4, "Sem")


def test_atualizar_dados_por_indice_passando_indice_menor_que_0():
    """
        Testar acessar index não existente da lista e atualizar dado nesse index
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")
    
    with pytest.raises(IndexError):
        lista.atualizar_elemento_por_indice(-1, "Sem")


def test_atualizar_dados_por_indice_passando_indice_como_string():
    """
        Testar acessar passar um index diferente de inteiro, e tentar atualizar o dado nesse index
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")
    
    with pytest.raises(ValueError):
        lista.atualizar_elemento_por_indice("1", "Sem")

