

"""
Módulo: methods.py

Objetivo: calcular quantos arquivos há neste ambiente virtual
"""

from datetime import datetime
from os import getcwd
from os import chdir, listdir
from typing import Union, Literal

def build_dict(the_key='key', the_value='value') -> dict:
    """
    To create a dictionary class
    :param the_key: can be any class, except: list, set
    :param the_value: can be any class
    :return: dict
    """
    return {the_key: the_value}


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


# Forma 1
def time_informer() -> None:
    the_hour = datetime.now().hour
    the_time = f'{the_hour}:{datetime.now().minute}:{datetime.now().second}'
    hours = (list(range(0, 24)))

    if the_hour in hours[0:12]:
        print(the_time, 'bom dia')
    elif the_hour in hours[12:18]:
        print(the_time, 'boa tarde')
    elif the_hour in hours[18:]:
        print(the_time, 'boa noite')
    del hours


# Forma 2
def time_informer2() -> str:
    the_hour = datetime.now().hour
    the_time = f'{the_hour}:{datetime.now().minute}:{datetime.now().second}'
    hours = (list(range(0, 24)))

    conditions = (
        [True if the_hour in hours[0:12] else False],
        [True if the_hour in hours[12:18] else False],
        [True if the_hour in hours[18:] else False],
    )

    answers = (f'{the_time}, bom dia :)', f'{the_time}, boa tarde', f'{the_time}, boa noite')
    the_result = answers[conditions.index([True])]

    return the_result


# Forma 3
def time_informer3() -> None:
    the_hour = datetime.now().hour
    the_time = f'{the_hour}:{datetime.now().minute}:{datetime.now().second}'
    hours = (list(range(0, 24)))

    conditions = [
        [f'{the_time}, bom dia :)' if the_hour in hours[0:12] else False],
        [f'{the_time}, boa tarde' if the_hour in hours[12:18] else False],
        [f'{the_time}, boa noite' if the_hour in hours[18:] else False],
    ]

    while [False] in conditions:
        conditions.pop(conditions.index([False]))

    print(*conditions[0])


def math_maker(
    value: Union[int, float],
    operator: Literal['+', '-', '*', '/', '**', '|'],
    value2: Union[int, float]
               ) -> None:
    square_operator = 0.5
    invalid_operator = '\n========== Erro ==========\nO operador fornecido é inválido:'
    invalid_cauculus = '\n========== Erro ==========\nDivisão por zero é inválida'

    try:
        if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':

            conditions = [
                [f'{value} + {value2} = {value + value2:,.2f}' if operator == '+' else None],
                [f'{value} - {value2} = {value - value2:,.2f}' if operator == '-' else None],
                [f'{value} x {value2} = {value * value2:,.2f}' if operator == '*' else None],
                [f'{value} / {value2} = {value / value2:,.2f}' if operator == '/' else None],
                [f'{value} ** {value2} = {value ** value2:,.2f}' if operator == '**' else None],
            ]

            while [None] in conditions:
                conditions.pop(conditions.index([None]))
            print("".join(conditions[0]))

        elif operator == '|':
            conditions = [(f'raiz de {value} = {value ** square_operator:,.2f}' if operator == '|' else None)]
            print("".join(conditions[0]))

        else:
            print(f'{invalid_operator} {operator!r}')

    except ZeroDivisionError:
        print(invalid_cauculus)


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


def word_counter(text: str = 'text') -> dict:
    """ Criar dicionário da quantidade de dados de uma string """
    container = {}
    counter = 0                                 # loop counter
    while counter < len(text):
        for letter in text:
            data = letter                       # creation of the variable which will represent the key
            data_countage = text.count(data)    # ............................................. the value
            container[data] = data_countage     # insertion of the key and its value
            counter += 1
    counter = 0
    return container


def word_counter2(text: str = 'text') -> dict:
    """ Criar dicionário da quantidade de dados de uma string """
    from collections import Counter
    container = Counter(text)
    return container


if __name__ == '__main__':
    pass
