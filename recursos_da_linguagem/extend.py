

"""
Módulo: extend.py
Objetivo: adicionar um dado em uma classe iterável lista

Observação:
    - apenas classes iteráveis podem ser adicionadas com esse método
    - aceita apenas um argumento por uso
    - pode ser usado multiplamente em linha
"""

# [ .extend() ] em linha
li = ['l']
li.extend('i'), li.extend('sta'),
print([1], li)

# [ .extend() ] em quebra de linha
li.extend('l')
li.extend('i')
li.extend('sta')
print([2], li)
