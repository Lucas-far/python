

"""
Módulo: nonetype.py
Objetivo: definir uma variável para ter um valor indefinido, para ser modificado futuramente
Observação:
    - em Python, uma var não pode ser declarada sem valor, então usa-se a classe do tipo sem tipo (NoneType)
"""


def encapirotar_nome(nome=None) -> str:  # não se sabe o nome, então define-se como 'nada'
    """"""
    return nome[::-1]

if __name__ == '__main__':
    print(encapirotar_nome('Lucas'))  # aqui o nome é definido
