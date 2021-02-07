

"""
Módulo: pprint.py
Objetivo: mostrar dados em iterável dispostos de forma vertical
"""

from pprint import pprint

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 7:Dissecando o Django User Model
    Aula:   # 68. Login e Autenticação
    Minuto: # 04:33
    """

# mudar os parâmetros para descobrir o que eles fazem
var = ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__',
       '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
       '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe',
       ]

print('\n')
pprint(var[:13], indent=5, compact=True)
print('\n')
pprint(var, indent=10, compact=True)
