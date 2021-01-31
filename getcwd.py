

"""
Módulo: getcwd.py
Objetivo: mostrar a rota atual no OS
Observação:
    - apesar de ser um método, ele retorna uma string, que pode ser concatenada com outras
"""

from os import chdir, getcwd

print([1], getcwd())
chdir(getcwd() + '/../')
print([2], getcwd())
chdir(getcwd() + '/../' + '/../')
print([3], getcwd())
