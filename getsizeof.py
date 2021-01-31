

"""
Módulo: getsizeof.py
Objetivo: retornar inteiro da quantidade de bytes em memória armazenados em um var ou dado literal
"""

from sys import getsizeof as _

def dizer_tamanho(classe, dado) -> None:
    print(classe, _(dado), 'bytes')

dizer_tamanho('booleano', True)
dizer_tamanho('complexo', 7j)
dizer_tamanho('dicionário', {'c': 'v'})
dizer_tamanho('flutuante', 7.0)
dizer_tamanho('inteiro', 7)
dizer_tamanho('lista', ['l'])
dizer_tamanho('nenhum', None)
dizer_tamanho('range', range(1, 4))
dizer_tamanho('conjunto', {'cj'})
dizer_tamanho('string', 's')
dizer_tamanho('tupla', ('t',))
