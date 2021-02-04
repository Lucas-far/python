

"""
Módulo: Literal.py
Objetivo: informar numa função, os tipos de retorno exatos que ela pode gerar, dentro de uma lista

Curso  # Programação em Python do básico ao avançado
Seção  # Seção 24:Novidades do Python 3.8
Aula   # 169. Tipos de dados mais precisos
Tempo  # 06:10
"""

from typing import Literal, Union

def teste_errado():
    """
    def dar_adjetivo(*, nome, sobrenome) -> Literal['viado(a)', 'arrombado(a)', 'travesti', 'machista', 'taxista',
                                                    'comunista', 'pedreiro(a)', 'drogado(a)']:
        adjetivos = [
            'viado(a)', 'arrombado(a)', 'travesti', 'machista', 'taxista', 'comunista', 'pedreiro(a)', 'drogado(a)'
        ]
        return f'{nome + " " + sobrenome}, você é um tremendo {choice(adjetivos)}'

    print(dar_adjetivo(nome='Lucas', sobrenome='Alfredo'))
    """

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
    math_maker(13, '*', 13.1)
