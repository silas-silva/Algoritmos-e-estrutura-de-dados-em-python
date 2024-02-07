from lista.ListaDuplamenteEncadeada import Lista
import pytest


def test_lista_nao_vazia():
    """
        Testar se a lista retorna falso para vazia, quando ela tem elementos
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")

    e_vazia : bool = lista.verificar_se_vazia()

    assert e_vazia == False


def test_lista_vazia():
    """
        Testar se a lista retorna true para vazia, quando ela está vazia
    """
    lista : Lista = Lista()

    e_vazia : bool = lista.verificar_se_vazia()

    assert e_vazia == True


def test_lista_vazia_depois_da_remocao_de_todos_os_elementos():
    """
        Testar se a lista retorna true para vazia, quando foi removido todos os elementos dela
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.deletar_primeiro()

    e_vazia : bool = lista.verificar_se_vazia()

    assert e_vazia == True