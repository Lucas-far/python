

"""
Módulo: ordereddict.py
Objetivo: não sei...
"""

from collections import OrderedDict

# Dois dicionários idênticos e ordenados, mas com chaves e valores fora de ordem
"OBS"  # Porém, por serem dicionários ordenados, não são considerados iguais
a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
b = OrderedDict({'b': 2, 'a': 1, 'c': 3})
print([1], f'{a == b = }')

# Dois dicionários idênticos e não ordenados, mas com chaves e valores fora de ordem
"OBS"  # Porém, por serem dicionários não ordenados, pode ser considerados iguais
c = {'a': 1, 'b': 2, 'c': 3}
d = {'b': 2, 'a': 1, 'c': 3}
print([2], f'{c == d = }')

# Dois dicionários, sendo o primeiro: ordenado, e o segundo: normal
"OBS"  # eles são considerados iguais
e = OrderedDict({'a': 1, 'b': 2})
f = {'b': 2, 'a': 1}
print([3], f'{e == f = }')
