

"""
Módulo: exist_ok.py
Objetivo: impedir o erro 'FileExistsError' em caso de criação de pasta repetida

Observações:
    - funciona com o método makedirs(), mas não funciona com o método mkdir()
    - makedirs() cria pastas aninhadas
    - mkdir() cria uma pasta única separada
"""

from os import chdir, getcwd, makedirs, mkdir

chdir(getcwd())

"OBS"  # Testar cada contexto de forma separada, comentando o inativo (#)

# Contexto que não gera erro, apenas ignorando o pedido de criar um diretório já existente (se já existir, obviamente)
makedirs('mkdir/mkdir2', exist_ok=True)

# Contexto que gera erro (se executado + de 1 vez), por não ser um parâmetro do método [ mkdir() ]
mkdir('mkdir')
makedirs('mkdir/mkdir2', exist_ok=True)
