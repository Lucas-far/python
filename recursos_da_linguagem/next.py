

"""
Módulo: next.py
Objetivo: usado em classes iteráveis para percorrer seus dados de forma específica, escolhendo saltá-los ou não
Observação:
    - não recomenda-se o uso em classe conjunto, pois o posicionamento dos dados é aleatório
"""

# @dict @list @range @set @str @tuple

s = iter('carpe diem')  # string tornando-se iterável pelo método [ iter() ], para poder usar [ next() ]
next(s), print(next(s), next(s)), next(s), next(s), next(s), next(s), print(next(s))
#                   a        r                                                   i
