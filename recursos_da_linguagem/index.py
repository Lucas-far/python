

"""
Módulo: index.py
Objetivo: retornar o número inteiro do índice de um caractere procurado, da esquerda para a direita

Observação:
    - O método possui de 1 até 3 parâmetros, sendo apenas o primeiro, mandatório

        EXEMPLO SINTAXE:
            var = []
            var.index('dado procurado', int=índice inicial, int=índice final)

    - Se o dado não existir no iterável alvo, o método gera [ ValueError ]
"""

# @list @range @string @tuple

"ex"  # Uso comum
print([2], range(1, 11).index(7))                       # 1 parâmetro
print([3], 'Habilidade'.index('l', 2))                  # 2 parâmetros
print([4], ('a', 'b', 'c', 'd', 'e').index('d', 1, 4))  # 3 parâmetros

"ex"  # Uso incomum, mas possível
print([1], ['item_lista', 'item_lista2'][0].index('t'))
