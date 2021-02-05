

"""
Módulo: discard.py
Objetivo: excluir um dado específico de uma classe conjunto
Observação:
    - se o dado a ser excluido não existir no conjunto, não retorna-se erro
    - pode ser usado multiplamente em linha
"""

# @set

print([1], cj := {False, None, True, '...'})
# Uso em quebra de linha
cj.discard(False)
cj.discard(None)
print([2], cj)
# Uso em linha
cj.discard(True), cj.discard('...')
print([3], cj)
