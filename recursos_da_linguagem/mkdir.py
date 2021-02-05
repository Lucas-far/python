

"""
Módulo: mkdir.py
Objetivo: criar um diretório em uma rota no sistema operacional alvo

Observação:
    - e comum usar [ mkdir() ] junto ao método chdir(), pois sempre se quer criar arquivos em um local específico
"""

from os import chdir, getcwd, mkdir

# Exemplo do método mkdir() através de um algoritmo criador de pastas
def folder_generator(the_path: str, name_matrix_dir: str = 'dir_matrix', quantity_dirs: int = 0) -> None:
    """
    Creates one dir and gets into it to create the dirs you specifiy
    :param the_path:        (str) the place in your OS to create the directories (dirs)
    :param name_matrix_dir: (str) the pattern name of the dirs which will be created for you
    :param quantity_dirs:   (int) how many directories you will want to be created
    :return: None
    """

    dir_for_storage = 0  # creates one dir to store the other dirs which you specify in [ quantity_dirs ]
    counter = 0
    while dir_for_storage < 1:
        chdir(the_path)
        mkdir(name_matrix_dir)
        chdir(getcwd() + f'/{name_matrix_dir}/')  # get into the one dir to start creating your dirs
        dir_for_storage += 1
        while counter <= quantity_dirs:
            mkdir(name_matrix_dir + str(counter))  # increment of the name of your dir with an integer, to avoid errors
            counter += 1

if __name__ == '__main__':
    folder_generator(the_path='/home/lucas/Desktop', name_matrix_dir='pasta', quantity_dirs=7)
