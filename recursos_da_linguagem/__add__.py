

"""
Módulo: __add__.py

Objetivo: executar subtração ou soma entre classes numéricas

Objetivo 2: adicionar dados à classes iteráveis: lista, string e tupla
"""

# @complex @float @int @list @str @tuple
print('[complexo]', c := 7j.__add__(3j))
print('[inteiro]', i := 7, i := i.__add__(3))
print('[flutuante]', f := 7.2, f := f.__add__(2.8))
print('[lista]', l := [], l := l.__add__([False, None, True]))
print('[string]', s := 'pyt'.__add__('hon'))
print('[tupla]', t := ('python',).__add__(('django',)))
