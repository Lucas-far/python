

"""
Módulo: exercicio_1
Objetivo: usar condições menores em forma de lista
"""

from typing import Literal, Union

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

if __name__ == '__main__':
    math_maker(13, '-', 13.1)
