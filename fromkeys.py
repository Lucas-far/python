

"""
Módulo: fromkeys.py
Objetivo: criação alternativa (incomum) de dicionário
Observação:
    - o argumento 1, deve ser iterável, e este sofre iteração
    - o argumento 2, não precisa ser iterável, mas se for iterável, sofrerá iteração
"""

print([1], {}.fromkeys('chave', ['valor']))
print([2], {}.fromkeys(['l', 'i', 's', 't', 'a'], None))
print([3], {}.fromkeys({*range(1, 4)}, (tuple(range(1, 4)))))
print([4], {}.fromkeys({False, None, True}, '...'))
print([5], {}.fromkeys('string', 0))
print([6], {}.fromkeys(('t', 'u', 'p', 'l', 'a',), 'tupla'))
