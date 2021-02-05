

"""
Módulo: in.py
Objetivo: palavra reservada para realizar loop for
Objetivo 2: checar se um dado é pertencente a um outro dado, gerando um booleano
Observação
    - O uso dessa sintaxe é útil somente com classes iteráveis
"""

# @list @range @str @tuple

"ex"  # objetivo
print([1], *[x.replace(x, f'{x + "-"}') for x in 'Albuquerque'])
print([2], [x.upper().split() if x == 'u' else x for x in 'Albuquerque'])
print([3], [{x} for x in enumerate('ok')])

"ex2"  # objetivo 2
print([4], [] in ['l'])
print([5], 7 in range(1, 11))
print([6], '_' in '_()')
print([7], 'a' in ('a', 'b', 'c'))
