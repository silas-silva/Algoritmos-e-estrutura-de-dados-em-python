from lista.ListaEncadeada import Lista
import pytest


# Classe para testar a busca
class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __eq__(self, outro_objeto: object) -> bool:
        return self.nome == outro_objeto.nome and self.idade == outro_objeto.idade


def test_buscar_elemento_na_lista():
    """
        Testar a busca de elementos na lista, passando um objeto como parâmentro
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    index : int = lista.buscar(Pessoa("Noé", 31))
    assert index == 1


def test_buscar_elemento_inexistente_na_lista():
    """
        Testar a busca de elementos na lista, passando um objeto que não está na lista como parâmentro
        O objeto não é encontrado, e a função retorna -1
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    index : int = lista.buscar(Pessoa("Thiago", 31))
    assert index == -1


def test_buscar_elemento_na_lista_depois_que_esse_elemento_foi_atualizado():
    """
        Testar a busca de elementos na lista, passando um objeto como parâmentro depois de ter mudado o objeto na posição original
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))
    # Atualizar objeto
    lista.atualizar_elemento_por_indice(1, Pessoa("Pedro", 40))
    
    elemento : int = lista.buscar(Pessoa("Pedro", 40))
    
    assert elemento == 1


def test_buscar_elemento_por_indice():
    """
        Testar a busca de elementos na lista passando um determinado indice
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    dado : Pessoa = lista.busca_por_indice(2)
    assert dado == Pessoa("Paulo", 32)


def test_buscar_elemento_por_indice_menor_que_0():
    """
        Testar a busca de elementos na lista passando um determinado indice inexistente
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    with pytest.raises(IndexError):
        lista.busca_por_indice(-2)


def test_buscar_elemento_por_indice_maior_que_tamanho_da_lista():
    """
        Testar a busca de elementos na lista passando um determinado indice inexistente
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    with pytest.raises(IndexError):
        lista.busca_por_indice(4)


def test_buscar_elemento_por_indice_indice_passando_string():
    """
        Testar a busca de elementos na lista passando um determinado indice com tipagem errada
    """
    lista : Lista = Lista()
    lista.adicionar(Pessoa("Pedro", 30))
    lista.adicionar(Pessoa("Noé", 31))
    lista.adicionar(Pessoa("Paulo", 32))
    lista.adicionar(Pessoa("Tiago", 33))

    with pytest.raises(ValueError):
        lista.busca_por_indice("2")



