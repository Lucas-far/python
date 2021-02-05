

"""
Módulo: choice.py

Objetivo: escolher um dos dados dentro de uma classe iterável
"""

from random import choice

# @list @range @str @tuple
print([1], l := ['l', 'i', 's', 't', 'a'], choice(l))
print([2], r := [*range(1, 11)], choice(r))
print([3], s := 'False', choice(s))
print([4], t := ('t', 'u', 'p', 'l', 'a'), choice(t))
