from app.ArvoreBinaria import ArvoreBinaria
from app.Inteiro import Inteiro


def test_adicionar_elemento_na_arvore():
    arvore : ArvoreBinaria = ArvoreBinaria()
    
    arvore.adicionar(Inteiro(1))
    arvore.adicionar(Inteiro(2))
    
    assert arvore.tamanho == 2


def test_remover_elemento_da_arvore():
    pass
