

"""
Módulo: items.py
Objetivo: mostrar dados de classe dicionário, de forma completa: chave e valor, em forma de tupla
Observação:
    - dicionários sob a influência do método, tornam-se incapazes de chamar chave
        1.1 para corrigir esse comportamento, o dicionário precisa receber cast (ver def detalhes)
"""

# @dict

# Diferença entre dicionário comum vs dicionário com o método [ .items() ]
print([1], {'a': 1, 'b': 2, 'c': 3})
print([2], {'a': 1, 'b': 2, 'c': 3}.items())        # o iterável perde característica de indexação na presença do método
print([3], list({'a': 1, 'b': 2, 'c': 3}.items()))  # para corrigir, usar [ cast ]

# Uso do método com loop for
d = {'a': 1, 'b': 2}

for key, value in d.items():  # não gera-se tupla
    print(key, value)

for value in d.items():       # gera-se tupla
    print(value)
