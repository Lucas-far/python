

"""
Módulo: contains.py

Objetivo:
    retornar [ True ou False ] para se um dado encontra-se dentro de uma classe iterável
    o método [ .__contains__() ] é similar a palavra reservada Python [ in ]
"""

# @dict @list @range @set @str @tuple
print([1], {1: 1}.__contains__(1))
print([2], [None].__contains__(None))
print([3], [*range(1, 8)].__contains__(7))
print([4], {*range(1, 8)}.__contains__(0))
print([5], 'string'.__contains__('T'))
print([6], ('tupla',).__contains__('inteiro'))

# Similaridade de [ .__contains__() ] com [ in ]
print([7], ('Brasil', 'America do Sul', 'Hemisfério Norte').__contains__('Brasil'))
print([8], 'Brasil' in ('Brasil', 'America do Sul', 'Hemisfério Norte'))
