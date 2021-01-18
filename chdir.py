

"""
Módulo: chdir.py

Objetivo: mudar diretório atual

Observação:
    1. é comum esse método ser mesclado com o método [ getcwd() ], que pertence a mesma biblioteca
    2. Sintaxe
        OS Windows
            separador de rota         --->  \\
            retornar um nível da rota ---> ..\\

        OS Ubuntu
            separador de rota         ---> /
            retornar um nível da rota ---> /../
"""

from os import chdir, getcwd

# @str

"No Windows"
# chdir('C:\\Users\\Lucas\\Downloads\\Main\\bdd_media')
# chdir('..')      # retorna um nível
# chdir('..\\..')  # retorna dois níveis

"No Ubuntu"
print([1], getcwd())                   # diretório atual deste arquivo
chdir(getcwd() + '/../')               # voltando um nível
print([2], getcwd())                   # diretório com um nível retornado
chdir('/home/lucas/PycharmProjects/')  # especificando um outro caminho manualmente
print([3], getcwd())                   # nova rota
chdir(getcwd() + '/../' + '/../')      # retornando dois níveis
print([4], getcwd())                   # nova rota modificada
