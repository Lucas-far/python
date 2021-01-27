

"""
Módulo: methods.py

Objetivo: calcular quantos arquivos há neste ambiente virtual
"""

from datetime import datetime
from os import getcwd

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
    # print(build_dict())
    print(file_counter(getcwd()))
    # print(make_data(7))
    # print(word_counter('Maria'))
    # print(word_counter2('Maria'))
    time_informer()
    print(time_informer2())
    time_informer3()
