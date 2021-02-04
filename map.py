

"""
Módulo: map.py
Objetivo: não sei o objetivo, precisa de mais pesquisa
"""

l = [9.4, 2.7, 5.6, 3.3, 2.9]
print([1], tuple(f"{x + 0.1:.1f}" for x in l))         # incrementar dados numéricos com [ comprehension ]
print([1], tuple(map(lambda v: f"{v + 0.1:.1f}", l)))  # incrementar dados numéricos com [ .map() ]
print([3], tuple(map(int, '2892458')))                 # converter cada dado iterável em inteiro
print([4], var := tuple(map(lambda v: v == 'a', 'Lucas')))  # analisar dados [ filter() é melhor ]
