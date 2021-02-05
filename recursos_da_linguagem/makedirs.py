

"""
Módulo: makedirs.py
Objetivo: criar pastas aninhadas, usando o separador de rota /
Observação:
    - o método possui parâmetro 2, que evita erro: FileExistsError
"""

from os import chdir, getcwd, makedirs

print([1], getcwd())
chdir(getcwd() + '/../')
print([2], getcwd())
makedirs('__pasta/__pasta2/__pasta3/')   # qualquer pasta passada que for repetida, gera-se [ FileExistsError ]
makedirs('pasta/pasta4', exist_ok=True)  # pastas repetidas serão ignoradas, pastas novas são criadas, aninhadas
