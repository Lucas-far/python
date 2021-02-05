

"""
Módulo: __len__.py
Objetivo: retornar a quantidade de dados/índices que uma classe iterável contêm
Observação:
    - não funciona com classes não iteráveis
"""

# @dict @list @range @set @str @tuple

print([1], {'chave': 'valor', 'chave2': 'valor2'}.__len__())
print([2], {False, None, True}.__len__())
