

"""
Módulo: difference.py
Objetivo: retornar os dados diferentes de uma variável conjunto, em relação à outras variáveis conjunto
"""

# @set

cj, cj2, cj3 = {0}, {0, 1}, {0, 1, 2}
print([1], resultado := {0, 1, 2, 3}.difference(cj, cj2, cj3))

"{0, 1, 2, 3}"  # conjunto que recebe o método (poderia estar declarado, mas está literal)
"OBS"           # o valor retornado (ou valores) deve ser aquele que não está em nenhum dos conjuntos comparados
"Resultado"     # o retorno seria 3, pois é o único que não aparece em nenhum dos conjuntos no escopo do método
