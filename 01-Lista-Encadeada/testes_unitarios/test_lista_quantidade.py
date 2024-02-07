from lista.ListaEncadeada import Lista
import pytest


def test_verificar_quantidade_com_lista_vazia():
    """
        Testar se é retornado o tamanho da lista, a mesma estando vazia
    """
    lista : Lista = Lista()

    quantidade : int = lista.obter_tamanho()

    assert quantidade == 0


def test_verificar_quantidade_de_elementos():
    """
        Testar se é retornado o tamanho da lista, quando inserido elementos de formas diferentes
    """
    
    lista : Lista = Lista()
    lista.adicionar(1)
    lista.adicionar(6)
    lista.adicionar_inicio(7)
    lista.adicionar_inicio(2)
    lista.adicionar_por_indice(indice=0, dado=9)
    lista.adicionar_por_indice(indice=4, dado=19)
    lista.adicionar_por_indice(indice=3, dado=21)

    quantidade : int = lista.obter_tamanho()

    assert quantidade == 7

