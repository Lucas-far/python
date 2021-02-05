

"""
Módulo: assert.py

Objetivo: palavra reservada para testar códigos em funções e seus parâmetros

Observação:
    1. Eu não sei se isso é exatamente um tipo de teste
"""

def mostrar_positivos(a: int = 1, b: int = 1, c: int = 1) -> tuple:
    assert a > 0 and b > 0 and c > 0, 'Há valores negativos'
    return a, b, c

def lanchonete(alimento: str) -> str:
    menu = {
            'sorvete de balnilha': 7.20,
            'suco de limão': 2.75,
            'bomba': 3.10,
            'caldo de cana': 5,
            'empada': 3.50,
            'churros de leite condensado': 4.20
    }

    assert alimento in menu, 'O cardápio não contém o alimento informado'
    return f'Você escolheu o alimento [ {alimento} ]'

if __name__ == '__main__':
    print(mostrar_positivos(1, 2, 3))
    print(mostrar_positivos(1, 2, - 3))  # segundo parâmetro é engatilhado
    print(lanchonete('bomba'))
    print(lanchonete('arroz'))           # segundo parâmetro é engatilhado (comentar 2 primeiras linhas desse escopo)
