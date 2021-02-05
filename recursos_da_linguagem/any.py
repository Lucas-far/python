

"""
Módulo: any.py

Objetivo:
    converter todos os dados dentro de variáveis iteráveis ou literais para booleano...
    se há pelo menos um dado = True, então o método retorna = True...
    Se todos os dados = False, então o método retorna = False

Observação:
    1. se o método receber um parâmetro que não é uma classe iterável, ele gera [ TypeError ]
"""

# @dict @list @set @str @tuple

print([1], f"{any({'': ''}) = }")
print([2], f"{any([]) = }")
print([3], f"{any({}) = }")
print([4], f"{any('') = }")
print([5], f"{any(()) = }")

# Quando há, entre os índices, algum verdadeiro = True
exemplo = [(), [], '', ' ']
for x in exemplo:
    print(f'O dado {x} é {any(x)}')
print([6], 'Resultado:', any(exemplo))

# Quando nenhum dos índices é verdadeiro = False
exemplo2 = [(), [], '']
for x in exemplo2:
    print(f'O dado {x} é {any(x)}')
print([7], 'Resultado 2:', any(exemplo2))
