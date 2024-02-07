from lista.ListaDuplamenteEncadeada import Lista
import pytest

def test_dados_foram_impressos_no_terminal():
    """
        Verificar se a função imprimir, que imprime elementos da lista está realmente imprimindo
    """
    lista : Lista = Lista()
    lista.adicionar("Noé")
    lista.adicionar("Moises")
    lista.adicionar("Pedro")
    
    imprimiu : bool = lista.imprimir()
    
    assert imprimiu == True