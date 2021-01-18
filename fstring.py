

"""
Módulo: fstring.py

Objetivo: mostrar/esconder partes decimais de cálculos através do recurso de f-string
"""

from typing import Union

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 170. Debugger mais simples com f-strings
    """

def elevar(um: Union[int, float] = 1, dois: Union[int, float] = 1) -> Union[int, float]:
    return um ** dois

if __name__ == '__main__':
    # var: Union[int, float] = elevar()
    print(elevar(2, 2.2))
    print(f'{elevar(2, 2.2):.1f}')
    print(f'{elevar(2, 2.2):.2f}')
    print(f'{elevar(2, 2.2):.3f}')
