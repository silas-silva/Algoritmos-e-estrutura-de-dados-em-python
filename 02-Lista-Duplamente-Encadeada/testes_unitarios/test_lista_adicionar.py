from lista.ListaDuplamenteEncadeada import Lista
import pytest


def test_adicionar_objeto_na_lista():
    """
        Testar a adição de elementos na lista
    """
    lista : Lista = Lista()
    lista.adicionar(2)

    # Foi adicionado 1 elemento
    assert lista.quantidade == 1


def test_adicionar_objeto_no_inicio_da_lista():
    """
        Testar a adição de elementos no inicio da lista
    """
    lista : Lista = Lista()
    lista.adicionar(1)
    lista.adicionar_inicio(2)
    # Para testar, vou remover o primeiro elemento e ver se é 2
    dado : int = lista.deletar_primeiro()
        
    assert dado == 2


def test_adicionar_objeto_no_inicio_da_lista_com_lista_vazia():
    """
        Testar a adição de elementos no inicio da lista dado que a lista esteja vazia
    """
    lista : Lista = Lista()
    lista.adicionar_inicio("Teste")
    
    assert lista.quantidade == 1


def test_adicionar_objeto_no_inicio_da_lista_por_indice():
    """
        Testar a adição de elementos no inicio da lista por indice
    """
    lista : Lista = Lista()
    lista.adicionar(1)
    lista.adicionar(2)
    lista.adicionar_por_indice(indice=0, dado=3)
    
    # Para testar, vou remover o primeiro elemento e ver se é 3
    dado : int = lista.deletar_primeiro()
        
    assert dado == 3


def test_adicionar_objeto_no_final_da_lista_por_indice():
    """
        Testar a adição de elementos no final da lista por indice
    """
    lista : Lista = Lista()
    lista.adicionar(1)
    lista.adicionar(2)
    ultima_posicao = lista.quantidade - 1
    lista.adicionar_por_indice(indice=ultima_posicao, dado=3)
    
    # Para testar, vou remover o primeiro elemento e ver se é 3
    dado : int = lista.deletar_ultimo()
        
    assert dado == 3


def test_adicionar_objeto_na_lista_por_indice():
    """
        Testar a adição de elementos em qualquer posição da lista
    """
    lista : Lista = Lista()
    lista.adicionar(1) # indice 0
    lista.adicionar(2) # indice 1
    lista.adicionar(5) # indice 2
    lista.adicionar(6) # indice 3
    lista.adicionar_por_indice(indice=2, dado=3)
    
    # Para testar, vou remover o primeiro o elemento de indice 2 e ver se é o novo dado colocado
    dado : int = lista.deletar_por_indice(2)
        
    assert dado == 3


def test_adicionar_objeto_na_lista_por_indice_com_lista_vazia():
    """
        Testar a adição de elementos na lista por indice, dado que a lista esteja vazia
    """
    lista : Lista = Lista()
    lista.adicionar_por_indice(indice=0, dado=1)
    
    assert lista.quantidade == 1


def test_adiciona_objeto_na_lista_por_indice_passando_string():
    """
        Testar a remoção por posição passando uma string invés de um número e esperar um ValueError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(ValueError):
        lista.adicionar_por_indice("2", 2)


def test_adiciona_objeto_na_lista_por_indice_passando_indice_menor_que_0():
    """
        Testar a remoção por posição passando um indice invalido e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(IndexError):
        lista.adicionar_por_indice(indice=-1, dado=2)


def test_adiciona_objeto_na_lista_por_indice_passando_indice_maior_que_a_lista():
    """
        Testar a remoção por posição passando um indice invalido e esperar um IndexError
    """
    lista : Lista = Lista()
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)

    with pytest.raises(IndexError):
        lista.adicionar_por_indice(indice=3, dado=3)