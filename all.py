

"""
Módulo: all.py

Objetivo:
    converter todos os dados dentro de variáveis iteráveis ou literais para booleano...
    se a conversão de todos os dados = True, então o método retorna = True...
    se há um dado = False, então o método retorna = False

Observação:
    1. se o método receber um parâmetro que não é uma classe iterável, ele gera [ TypeError ]
"""

# @dict @list @set @str @tuple

print([1], f"{all({'': ''}) = }")
print([2], f"{all([]) = }")
print([3], f"{all({}) = }")
print([4], f"{all('') = }")
print([5], f"{all(()) = }")
