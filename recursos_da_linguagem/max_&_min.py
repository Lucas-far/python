

"""
Módulo: max_&_min.py
Objetivo: retornar o dado mínimo em uma classe iterável, especificando início ou início e fim
Objetivo 2: retornar o dado máximo em uma classe iterável, especificando início ou início e fim

Observação:
    - o método, por padrão, age procurando o menor ou maior dado dentro de um iterável
    - o método, pode fazer uma varredura mais específica, se um slice for especificado
    - uso em strings, min() filtra o menor dado alfabético, e max() filtra o maior
"""

r = [*range(1, 8)]

print([1], r, max(r))
print([2], r, min(r))
print([3], r[2:], max(r[2:]))
print([4], r[2:8], min(r[2:8]))
print([5], r[1::3], max(r[1::3]))
print([6], r[2:6:3], min(r[2:6:3]))
print([7], r[:5], max(r[:4:7]))
