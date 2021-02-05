

"""
Módulo: count.py

Objetivo: retornar a classe inteiro de quantas vezes um dado iterável repete-se dentro de uma classe iterável

Observação:
    1 - pode ser usado em classe range, mas não faz sentido, a não ser que sejam usados vários ranges
"""

# @list @range @str @tuple
print([1], [False, None, True].count(False))
print([2], 'kk...'.count('k'))
print([3], ('tupla', 'tupla', 'tupla', 'Tupla').count('tupla'))
