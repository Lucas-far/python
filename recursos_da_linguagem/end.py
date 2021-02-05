

"""
Módulo: end.py
Objetivo: alterar exibição em iteração de vertical para horizontal, com a opção de adição de um espaçador entre os dados
"""

# Dados na vertical (padrão)
r = {*range(1, 4)}
for obj in r:
    print('*', obj)

# Dados na horizontal
for obj in r:
    print(obj, end='*')  # * = separador

print('\n')

# Dados na horizontal (elementos dentro do end="")
for obj in r:
    print(end=f'{obj}*')
