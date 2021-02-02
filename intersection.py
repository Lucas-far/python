

"""
Módulo: intersection.py
Objetivo: comparar e retornar dados idênticos de uma var conjunto alvo em relação a outra(s) passadas como parâmetro
"""

# @set

print([1], {False, None, True}.intersection({8, 9, 10}))           # retorno quando não há qualquer similaridade
print([2], {False, None, True}.intersection({('t',), 's', None}))  # retorno quando há qualquer similaridade

# Explicação mais detalhada
var = {'a', 'e', 'i', 'o', 'u'}
print([3], var.intersection({'a', 'x'}, {'a', 'u'}))  # se há 2+ sets comparados, o dado achado precisa estar nos 2
print([4], var.intersection({'a', 'x'}, {'l', 'u'}))  # o dado 'a', está no 1, mas não está no 2, então não é validado
