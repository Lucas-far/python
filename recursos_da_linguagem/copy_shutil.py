

"""
Módulo: copy_shutil.py

Objetivo: copiar um arquivo, de seu caminho atual para duplicá-lo em outro

Observação:
    o método possui 2 args mandatórios
    argumento 1 ---> especifica-se a rota do arquivo a ser deslocado + sua extensão
    argumento 2 ---> especifica-se a nova rota

Sintaxe:
    No OS Windows ---> \\
    No OS Ubuntu  ---> /
"""

from shutil import copy

# @str

"Windows"  # copy('C:\\Users\\Lucas\\Desktop\\video.mp4', 'C:\\Users\\Lucas\\Downloads')

"Ubuntu"
copy('/home/lucas/Documents/css_botao', '/home/lucas/Desktop')
