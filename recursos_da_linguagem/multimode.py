

"""
Módulo: multimode.py
Objetivo: retornar dado que mais ocorre dentro de uma var lista
Observação:
    - pode ser usada em classe conjunto e dicionário, mas é irrelevante, pois ambas não permitem repetição de dados
"""

# @dict @list @range @set @str @tuple

from statistics import multimode

print([1], multimode(['a', 'b', 'c', None, None, None]))
# Caso não haja dados reincidentes ou reincidentes iguais, todos são retornados
print([2], t := multimode(('a', 'b', 'c', None, True, False)))
