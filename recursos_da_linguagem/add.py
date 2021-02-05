

"""
Módulo: add.py

Objetivo: anexar um novo dado à uma variável de classe conjunto

Observação:
    1. pode ser usado multiplamente em linha, se separado por vírgula
    2. o método aceita somente um parâmetro por uso
    3. classe conjunto é intolerante às classes: conjunto, dicionário e lista
"""

# @set

"[ add() ] em linha"
print([1], cj := set({}))
cj.add(False), cj.add(None), cj.add(True)
print([1], cj)

"[ add() ] em quebra de linha"
print([2], cj2 := set({}))
cj2.add(False)
cj2.add(None)
cj2.add(True)
print([2], cj2)
