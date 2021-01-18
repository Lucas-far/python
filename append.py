

"""
Módulo: append.py

Objetivo: anexar qualquer tipo de classe à uma variável de classe lista

Observação:
    1. pode ser usado multiplamente em linha (separação por vírgula)
    2. dados iteráveis com + de 1 índice, quando adicionados por esse método, contam apenas como 1 índice
"""

# @list

"[ append() ] em linha"
print([1], l := [])
l.append(False), l.append(None), l.append(True)
print([2], l)

"[ append ] em quebra de linha"
print([3], l2 := [])
l2.append(False)
l2.append(None)
l2.append(True)
print([4], l2)
