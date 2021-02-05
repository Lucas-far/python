

"""
Módulo: mean.py
Objetivo: retornar a média entre classes inteiras ou flutuantes, misturadas ou separadas, dentro de um iterável
"""

# @dict @list @range @set @tuple

from statistics import mean

print([1], mean([5, 10, 15, 20, 25, 30]))
print([2], mean({99, 16.4, 7.75, 86.1, 51.6}))
print([3], mean((1.7, 2.7, 3.7, 4.7, 5.7)))
