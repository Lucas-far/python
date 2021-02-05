

"""
Módulo: Counter.py

Objetivo: gerar um dicionário da quantidade de vezes que cada um dos dados em uma classe iterável, repete-se
"""

from collections import Counter
from methods import make_data as data_

# @dict @list @range @set @str @tuple

print([1], Counter({False: not True, None: None, True: not False}.keys()))    # @dict
print([2], Counter({False: not True, None: None, True: not False}.values()))  # @dict
print([3], Counter([False, not True, None, None, True, not False]))           # @list
print([4], Counter([*range(1, 8)]))                                           # @range

"Lembrete"  # Como o método [ make_data ] retorna uma lista, então é preciso usar comprehension para outras classes

print([5], Counter(set(obj for obj in data_(3))))                             # @set
print([6], Counter(f'{data_(3)}'))                                            # str
print([7], Counter(tuple(obj for obj in (data_(3)))))                         # tuple
