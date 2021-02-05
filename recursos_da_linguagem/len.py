

"""
Módulo: len.py
Objetivo: retornar a quantidade de dados/índices que uma classe iterável contêm
"""

# @dict @list @range @set @str @tuple

print([1], len({False, None, True}))
print([2], len(s := 'string'))

# Estranhezas relacionadas ao método, se usado com a classe conjunto
print(len({False, 0}))  # aqui deveria ser 2, mas é 1, pois False = 0, e em conjunto dados repetidos não contam
print(len({True, 1}))   # idem......................., pois True = 1, e em conjunto dados repetidos não contam
print(len({1, 1.0}))    # idem......................., pois float int = int, e em conjunto dados repetidos não contam
