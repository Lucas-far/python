

"""
Módulo: __dict__.py

Objetivo: retornar um dicionário de todos os atributos de instância de um objeto instanciado
"""

class Bandeira:
    def __init__(self, cores: list = [], altura_largura: tuple = ()):
        self.cores = cores
        self.altura_largura = altura_largura

if __name__ == '__main__':
    print(Bandeira(['verde', 'amarelo', 'azul', 'branco'], (12, 24)).__dict__)
