

"""
Módulo: appendleft.py

Objetivo: anexar qualquer tipo de classe à uma variável de classe deque/lista, a partir do índice 0 (sempre)

Observação:
    1. a classe [ deque ] têm a mesma biblioteca de métodos da classe [ lista ], mas com métodos adicionais
    2. pode ser usado multiplamente em linha (separação por vírgula)
    3. dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice
"""

from collections import deque

# @deque

"[ appendleft() ] em linha"
print([1], d := deque([]))
d.appendleft(False), d.appendleft(None), d.appendleft(True)
print([2], d)

"[ appendleft() ] em quebra de linha"
print([3], d2 := deque([]))
d2.appendleft(False)
d2.appendleft(None)
d2.appendleft(True)
print([4], d2)
