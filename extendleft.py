

"""
Módulo: extendleft.py
Objetivo: adicionar um dado iterável em uma classe deque, no índice 0
Observação:
    - apenas classes iteráveis podem ser adicionadas com esse método
    - aceita apenas um argumento por uso
    - pode ser usado multiplamente em linha
"""

from collections import deque

# [ .extendleft() ] em linha
dq = deque(['l'])
dq.extendleft('i'), dq.extendleft('sta')
print([1], dq)

# [ .extendleft() ] em quebra de linha
dq.extendleft('ats')
dq.extendleft('i')
dq.extendleft('l')
print([2], dq)
