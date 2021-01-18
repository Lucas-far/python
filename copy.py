

"""
Módulo: copy.py

Objetivo: clonar dados de um iterável para outro, sem gerar um elo entre os dados envolvidos
"""

# @dict @list @set
print([1], d := {'Nome': 'Juvêncio', 'ciclista': True}, [2], d2 := d.copy(), d2.popitem(), [3], d2, [4], d)
print([2], l := ['dó', 'ré', 'mi'], l2 := l.copy())
print([3], cj := {False, None, True}, cj2 := cj.copy())
