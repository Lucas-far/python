

"""
Módulo: fmean.py
Objetivo: retornar a média de números reais (flutuantes)
Objetivo 2: retornar a média de números inteiros exatos, na sua forma flutuante
Observação:
    - como cálculo de média necessita mais de um valor, então o método só funciona com dados dentro de iteráveis
    - com fmean(), o retorno sempre será flutuante, independente de ser real ou não
    - com mean(), o retorno sempre será inteiro, independnente de ser real ou não
"""

from statistics import fmean, mean

# Diferença de comportamento dos métodos em relação à presença de valores não reais
print([1], 'fmean ||', fmean([1, 2, 3]))
print([2], 'mean  ||', mean([1, 2, 3]))
print([3], 'fmean ||', fmean([1.1, 2.2, 3.3]))
print([4], 'mean  ||', mean([1.1, 2.2, 3.3]))
