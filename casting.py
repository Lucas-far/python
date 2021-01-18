

"""
Módulo: casting.py

Objetivo: converter uma classe para outra
"""

print([1], set((1, 2, 7)))                   # tupla para conjunto
print([2], list({*range(1, 11)}))            # conjunto para lista
print([3], i := '123', int(i))               # string para inteiro
print([4], ''.join(['abc']))                 # lista para string
print([5], tuple({'Python': True}.items()))  # dicionáriro para tupla
