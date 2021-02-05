

"""
Módulo: clear.py

Objetivo: esvaziar dados de classes iteráveis específicas
"""

# @dict @list @set
print([1], d := {'dict': {}}, d.clear(), d)
print([2], l := ['...'], l.clear(), l)
print([3], cj := {'set'}, cj.clear(), cj)
