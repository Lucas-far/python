

"""
Módulo: listdir.py
Objetivo: mostrar uma lista dos diretórios e módulos existentes em uma rota especificada
"""

from os import chdir, listdir

def show_dir_files(the_path: str) -> None:
    """
    Go to a path and display files in it
    :param the_path: str (the exact path of your OS to reach target files)
    :return: None
    """
    chdir(the_path)
    list_the_path_files: tuple = tuple(enumerate(listdir()))  # files gathered
    for index, file in list_the_path_files:                   # display files by numbers and name
        index = index + 1
        print(f'arquivo: {index} || nome: {file}')

if __name__ == '__main__':
    show_dir_files(the_path='/home/lucas/PycharmProjects/')
