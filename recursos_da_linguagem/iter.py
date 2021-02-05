

"""
Módulo: iter.py
Objetivo: tornar uma variável iterável, capaz de chamar dados de forma singular, sem usar indexação

Observação:
    - O método torna a variável percorrível singularmente, mas depende de outro método: next()
    - Se o método next() não for usado junto, mostra-se apenas um objeto de memória
    - Se for tentado usar indexação, gera-se [ TypeError ]
    - Funciona em dicionário, mas é desnecessário
    - Funciona em conjunto, mas a iteração é aleatória, portanto, não será controlada
    - Para não exibir um dado, usa-se [ next(var) ], e para exibir: [ print(next(var)) ]
"""

# @dict @list @range @set @str @tuple

print(d := iter({1: 'a', 2: 'b', 3: 'c'}))
next(d), next(d), print(next(d))  # salto, salto, exibição

print(s := iter('Farias'))
next(s), print(next(s)), print(next(s)), print(next(s))  # salto, exibição, exibição, exibição
