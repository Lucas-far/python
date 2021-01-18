

"""
Módulo: methods.py

Objetivo: calcular quantos arquivos há neste ambiente virtual
"""

def file_counter(the_path_string):
    """"""
    from os import scandir

    the_path = tuple(scandir(the_path_string))
    the_result = [str(item.is_file()) for item in the_path].count('True')
    return f'Há {the_result} arquivos em {the_path_string}'

def make_data(index=1):
    """"""
    from uuid import uuid4
    box = []
    counter = 0
    while counter < index:
        box.append(f'{uuid4()}'[:3])
        counter += 1
    counter = 0
    return box

if __name__ == '__main__':
    from os import getcwd
    print(var := file_counter(getcwd()))
    print(var2 := make_data(7))
