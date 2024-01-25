from app.ArvoreBinariaRecursiva import ArvoreBinariaRecursiva
from app.Inteiro import Inteiro


def test_adicionar_elemento_na_arvore():
    arvore : ArvoreBinariaRecursiva = ArvoreBinariaRecursiva()
    
    arvore.adicionar(Inteiro(1))
    arvore.adicionar(Inteiro(2))
    
    assert arvore.tamanho == 2


def test_remover_elemento_da_arvore():
    pass
