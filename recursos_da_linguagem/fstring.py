

"""
Módulo: fstring.py
Objetivo: usar variados tipos de recursos que podem ser usados dentro de uma fstring
"""

from random import randint
from typing import Union

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 170. Debugger mais simples com f-strings
    """

# Recursos da linguagem dentro de fstring
print([1], f'{(s := "Carlos")}')                                      # declaração walrus
print([2], f'{(l := "aeiou".split()) = }')                            # declaração walrus + =
print([3], f'{[x for x in "Augusto"] = }')                            # comprehension
print([4], f'{"".join(list(filter(lambda y: y != "v", "var"))) = }')  # filter
print([5], f"{[x / randint(1, 5) for x in range(7, 11)] = }")         # loop for

# loop for com if & else
print([6], f"{''.join(['Certo :)' if len('string') == randint(1, 6) else 'Errado, é {} :('.format(len('string'))]) = }")

# exemplo de debugger
print([7], f"{('string'.split()) == ['string']}")

def elevar(um: Union[int, float] = 1, dois: Union[int, float] = 1) -> Union[int, float]:
    return um ** dois

if __name__ == '__main__':
    ""  # var: Union[int, float] = elevar()
    # Usando fstring para restringir casas decimais de cálculos flutuantes
    print([8], elevar(2, 2.2))
    print([9], f'{elevar(2, 2.2):.1f}')
    print([10], f'{elevar(2, 2.2):.2f}')
    print([11], f'{elevar(2, 2.2):.3f}')
    # Usando fstring para restringir casas decimais de cálculos flutuantes + adição de separador
    print([12], f'{elevar(7, 3.7)}')       # valor original
    print([13], f'{elevar(7, 3.7):,.1f}')  # valor com 4 casas com separação por vírgula e 1 casa decimal
    print([14], f'{elevar(7, 5.7):,.2f}')  # valor com 5 casas com separação por vírgula e 2 casas decimais
    print([15], f'{elevar(7, 6.7):,.3f}')  # valor com 6 casas com separação por vírgula e 3 casas decimais
    print([16], f'{elevar(7, 7.2):,.4f}')  # valor com 7 casas com separação por vírgula e 4 casas decimais
