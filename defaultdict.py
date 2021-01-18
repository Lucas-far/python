

"""
Módulo: defaultdict.py

Objetivo: nesse contexto específico, criar várias chaves com um único valor, através de uma chave = função lambda

Observação:
    1. através da palavra reservada lambda, cria-se um valor padrão para qualquer chave nova criada
    2. chaves são criadas pelos contextos: declaração e print
"""

from collections import defaultdict

print([1], d := defaultdict(lambda: None))
d['a']          # Criação de uma chave sem variável
print(d['b'])   # Criação de uma chave sem variável em print
novo = d['c']   # Criação de uma chave em variável
print([2], d)
d['b'] = False  # Após declarados, os dados podem ser editados
d['c'] = True
print([3], d)
