

"""
Módulo: hypot.py
Objetivo: calcular hipotenusa
Observação:
    - dados iteráveis podem ser usados com o método, se forem descompactados
    - a lógica do método recebe 2 parâmetros, mas não gera erro se mais de 2 forem adicionados
"""

from math import hypot

# @float @int

print([1], hypot(10, 20))
print([2], hypot(10.10, 20.20))
# usando o método com iteráveis descompactados
print([3], hypot(*{10, 20}))
print([4], hypot(*[10, 20]))
print([5], hypot(*(10, 20)))
