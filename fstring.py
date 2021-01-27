

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

# Usando fstring para restringir casas decimais de cálculos flutuantes
if __name__ == '__main__':
    # var: Union[int, float] = elevar()
    print(elevar(2, 2.2))
    print(f'{elevar(2, 2.2):.1f}')
    print(f'{elevar(2, 2.2):.2f}')
    print(f'{elevar(2, 2.2):.3f}')
