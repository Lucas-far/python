

"""
Módulo: move.py
Objetivo: modificar um arquivo do seu local atual, no OS
Sintaxe:

    move('/par1=rota atual + nome do arquivo.formato', 'par2=nova rota do módulo')

Observação:
    - sintaxe de rota para o Windows: \\
    - sintaxe de rota para o Ubuntu: /
    - a escrita da rota pode ser toda em minúscula, mas não deve conter erros de digitação
"""

from shutil import move

"move('C:\\Users\\Lucas\\Downloads\\a.png', 'C:\\Users\\Lucas\\Downloads\\main')"  # sintaxe em Windows

#move('rota atual + nome.formato', 'rota nova do arquivo'
move('/home/lucas/Pictures/a.png', '/home/lucas/Videos')                           # sintaxe em Ubuntu
