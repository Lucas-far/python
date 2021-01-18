

"""
Módulo: del.py

Objetivo: deletar uma variável declarada
"""

b, i, l = True, 0, ['list', 'list2']

print(b)
del b
# print(b)

print(i)
del i
# print(i)

print(l)
del l[1]
print(l)
del l[0]
print(l)
del l
# print(l)
