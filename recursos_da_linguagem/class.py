

"""
Módulo: class.py

Objetivo: mostrar a classe de um dado, seja declarado ou literal
"""

# @global

def mostrar_classe(classe, dado):
    try:
        return classe, dado.__class__
    except AttributeError as error:
        return '{}{}{}'.format('\033[1:31m', error, '\033[m')

if __name__ == '__main__':
    print(mostrar_classe('booleano', True))
    print(mostrar_classe('complexo', -7j))
    print(mostrar_classe('dicionário', {-7: -7}))
    print(mostrar_classe('flutuante', -7.0))
    print(mostrar_classe('inteiro', -7))
    print(mostrar_classe('lista', [-7]))
    print(mostrar_classe('nenhum', None))
    print(mostrar_classe('range', range(-7, -6)))
    print(mostrar_classe('conjunto', {-7}))
    print(mostrar_classe('string', '-7'))
    print(mostrar_classe('tupla', (-7,)))
