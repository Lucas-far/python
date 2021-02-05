

"""
Módulo: bin.py

Objetivo: converter classe inteira para sua versão binária

Observação:
    1. os dois primeiros índices do retorno do método, não fazem parte da conversão, então eles são ignorados
"""

# @int
print([1], str(bin(70))[2:])  # converte-se para string, para poder omitir os dois primeiros índices
print([2], format(70, 'b'))   # Exemplo alternativo de mesmo resultado
