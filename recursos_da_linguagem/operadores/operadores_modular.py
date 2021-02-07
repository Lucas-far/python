

"""
Módulo: operadores_modular.py
Objetivo: verificar se um número é par ou ímpar
Objetivo 2: analizar iteráveis para filtrar dados
"""

# Método simples para exemplificar uso de operador módular
def check_odd_or_even(*args) -> None:
    """
    Place numbers into a tuple and check each one in order to know if they are odd or even
    :param args:
    :return:
    """
    for obj in args:
        if not obj % 2:  # if divisible by 2
            print(f'O número {obj} é par')
        else:
            print(f'O número {obj} é ímpar')


if __name__ == '__main__':
    check_odd_or_even(10, 19, 22, 7, 11, 4)

    # Outros exemplos de operações modulares
    "EXEMPLO 1"
    print([1], [x for x in [*range(1, 28)] if x % 7 == 0])  # de 1 a 27, pegar divisíveis por 7
    print([2], [x for x in [*range(1, 28)] if not x % 7])   # ....................................
    "EXEMPLO 2"
    print([3], [x for x in [*range(1, 28)] if x % 2])       # de 1 a 27, pegar não divisíveis por 2
    print([5], [x for x in [*range(1, 28)] if x % 2 == 1])  # .....................................
    "EXEMPLO 3"
    print([4], [x for x in [*range(1, 28)] if not x % 2])   # de 1 a 27, pegar divisíveis por 2
    print([6], [x for x in [*range(1, 28)] if x % 2 == 0])  # .................................
