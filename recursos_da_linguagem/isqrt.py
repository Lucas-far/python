

"""
Módulo: isqrt.py
Objetivo: retornar a raiz quadrada de um valor inteiro
Objetivo 2: retornar a parcela inteira de um valor inteiro que não possui raiz exata,

Observação:
    - tanto para o objetivo 1 e 2, os valores podem estar sozinhos ou em um iterável que contenha somente inteiros

    EXEMPLO sobre objetivo 2:
       - 10 não têm uma raiz exata
       - o método isqrt() faz cálculos até chegar ao inteiro, cuja multiplicação é a mais próxima de 10...
       - o mais próximo é [ 3 x 3 = 9 ], então: isqrt(10) seria 3
"""

from math import isqrt

# exemplo com valores de raiz exata
print([1], isqrt(25))
print([2], i := isqrt(36))
print([3], [isqrt(index) for index in [9, 169, 64, 100, 144]])
print([4], tuple((isqrt(index) for index in (225, 484, 729))))

# exemplo com valores de raiz não exata
print([5], {isqrt(each_number) for each_number in [10, 20, 30, 40, 50]})
