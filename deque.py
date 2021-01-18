

"""
Módulo: deque.py

Objetivo: forma alternativa e melhorada de usar a classe lista

Observação:
    A classe deque é a classe lista, só que além de ter abiblioteca de lista, tambem têm suas próprias
"""

from collections import deque

print([1], dq := deque([]))  # Instanciação de um deque

# Exemplos de bibliotecas em lista e deque
dq.append(False)
dq.extend('...')

# Exemplos de bibliotecas apenas para deque
dq.appendleft(True)
dq.extendleft('None')

print([2], dq)
